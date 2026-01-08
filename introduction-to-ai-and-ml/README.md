# Queues

In this module we will be introducing the learners to the concepts of AI & ML, and the latest advances in the field.

We will discuss what AI & ML is and when you might consider using these to solve problems, as well as some of the associated considerations that should be taken when implementing AI & ML solutions.

We will live demo the creation of a document summarisation & querying script using OpenAIs GPT model. Learners will be able to ask documents questions, and get answers based on the content of the documents.

## Overview

- General overview of AI space
- ML and it's applications
- Deep Learning
- Generative AI and it's augmentations
- Live demo of OpenAIs GPT API to summarise & query documents

## Timings

- This session is timetabled for 1 block at 1.5 hrs each, i.e. 0.25 elapsed training days
- The formative assessments occur during this and are included in that timing

## Assessments

To check the learner progress in this session we have:

- Multiple Quizzes throughout the session with answer walkthrough
- Follow along demo for the students

## Prep

- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises
- Demo will require Python 3.9 and installation of the requirements.txt in the demo folder
- Prior to the session, you would need to obtain an OpenAI API Key (at the moment of creation of the session they gave $120 to use for developers) you can sign up for an account here: https://openai.com
- The OpenAI API Key would then needs to be stored in AWS Secrets Manager with Secret name as "OpenAI-API-Key" and should be stored as "{"Authorisation":"open-ai-api-key"}"

### Demo Prep

The demo shows how to utilise LLMs to summarise pdf documents and how to use LLMs in conjunction with a Vector DB to ask pdf documents questions.

- Demo will require a Python 3.9 venv and installation of the `handouts/requirements.txt` file
- Make sure to run `aws sso login --profile <profile_name>` so that the script can retrieve the API Key from AWS Secrets Manager
- The demo usually takes around 30 minutes
- Start from `handouts/demo_template.py` and work towards `handouts/demo_final.py`
- If you are pressed for time, you can also walk through `handouts/demo_final.py` explaining the different parts of the solution
- As part of asking questions to the document showcase both asking for information that is in the PDF articles and the information that is not e.g: What were the sales of GTA 5 in the first 3 days? - information present in the article, What were the sales of GTA 4 in the first 3 days? - No reference to this is the article, but a very similar question.

## Session

- Run the presentation
- Both the template and the final versions are available in the handouts folder
- The demo shows how you can utilise LLMs to summarise pdf documents and how to use LLMs in conjunction with a Vector DB to ask pdf documents questions.
