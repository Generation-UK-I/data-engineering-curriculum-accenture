import json
import textwrap
import time
import boto3
import glob
import os
from botocore.exceptions import ClientError
from dotenv import load_dotenv, find_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.chains.summarize import load_summarize_chain
from langchain import OpenAI

from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import PyPDFDirectoryLoader

index = None

def get_secret():

    secret_name = "OpenAI-API-Key"
    region_name = "eu-west-1"

    # Create a Secrets Manager client
    session = boto3.session.Session(profile_name='generation')
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    # Retrieve the secret
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        openai_api_key = json.loads(get_secret_value_response['SecretString'])['Authorisation']
    except ClientError as e:
        raise e
    
    with open('.env', 'w') as file:
        file.write(f"OPENAI_API_KEY={openai_api_key}")
        
# Handle menu options
def menu_options():
    print('\n')
    print("1. Generate general summaries")
    print("2. Ask documents a question")
    print("3. Exit")
    while True:
        try:
            choice = int(input("Enter your choice [1-3]: "))
            return choice
        except ValueError:
            print("Invalid choice. Try again")

# Summarize a document 
def summarize_documents():
    summaries = []
    for pdf_file in glob.glob("docs/*.pdf"):
        loader = PyPDFLoader(pdf_file)
        split_pdf = loader.load_and_split()
        chain = load_summarize_chain(llm, chain_type="map_reduce")
        summary = chain.run(split_pdf)
        summaries.append(summary)
    with open("summaries/GeneralSummaries.txt", "w") as file:
        for summary in summaries:
            file.write("\n".join(textwrap.wrap(summary)))
            file.write("\n"*3)

# Load documents into vectorstore    
def load_documents_to_vectorstore():
    loader = PyPDFDirectoryLoader('docs')
    global index
    index = VectorstoreIndexCreator().from_loaders([loader])
            
# Ask documents a question 
def ask_documents_a_question():
    print('What is your question?')
    question = input()
    answer = index.query(question)
    print('Answer: ', answer)

# Main script entry point
if __name__ == "__main__":
    # Get OpenAI API key from AWS Secrets Manager
    get_secret()
    load_dotenv(find_dotenv())
    
    # Set up OpenAI client
    llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY') , temperature=0.2)
    
    # Load documents into vectorstore
    load_documents_to_vectorstore()
    
    while True:
        choice = menu_options()
        if choice == 1:
            print("Generating summaries")
            print('\n')
            summarize_documents()
        elif choice == 2:
            print("Ask documents a question")
            print('\n')
            ask_documents_a_question()
        elif choice == 3:
            print("Exiting")
            break
        else:
            print("Invalid choice. Try again")
        time.sleep(4)
