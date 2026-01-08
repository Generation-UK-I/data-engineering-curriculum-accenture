import json
import textwrap
import time
import boto3
import glob
import os
from botocore.exceptions import ClientError
from dotenv import load_dotenv, find_dotenv

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

# Main script entry point
if __name__ == "__main__":
    # Get OpenAI API key from AWS Secrets Manager
    get_secret()
    load_dotenv(find_dotenv())
    
    while True:
        choice = menu_options()
        if choice == 1:
            print("Generating summaries")
            print('\n')
        elif choice == 2:
            print("Ask documents a question")
            print('\n')
        elif choice == 3:
            print("Exiting")
            break
        else:
            print("Invalid choice. Try again")
        time.sleep(4)
