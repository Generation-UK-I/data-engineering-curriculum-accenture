# Pub/Sub

In this module we will be introducing the learners to pub/sub. We will discuss what a pub/sub is and why you might want to use one, as well as some of the associated considerations that should be taken and design patterns that can be implemented. We will live demo the creation of a topic, subscription, send message to a topic and receive the message as a subscriber. Learners will be asked to integrate pub/sub into the existing codebase for their projects.

## GCP session order

Related sessions are:

- Intro To Cloud (External speaker, 1.5 hrs)
- [GCP Introduction](../gcp-01-introduction/README.md) - 1.25 days
- [GCP Data Lakes with GCS](../gcp-02-data-lakes/README.md) - 0.25 days
- [GCP Data Warehousing with BigQuery](../gcp-03-data-warehousing/README.md)- 0.25 days
- [DevOps with GCP inc CI & CD](../gcp-04-devops/README.md) - 0.25 days
- [GCP with Terraform for CD](../gcp-05-terraform/README.md) - 0.25 to 0.5 days
- [Monitoring GCP](../gcp-06-monitoring/README.md) - 0.5 days
- [GCP Queues - Pub/Sub](../gcp-07-pub-sub/README.md) - 0.5 days
- [GCP Data Streams with DataFlow](../gcp-08-data-streams/README.md) - 0.5 days
- [Final Project Inception with GCP](../gcp-09-final-project/README.md) - 0.5 days

There is a public organisation with repos of code demos:

- <https://github.com/JLR-DE-Academy>

## Overview

- Messaging Queues
- Event Driven Design
- Pub/Sub Model

## Timings

- This session is timetabled for 2 blocks at 1.5 hrs each, i.e. 0.5 elapsed training days
- The formative assessments occur during this and are included in that timing
- The exercises for this session are also included in that time

## Assessments

To check the learner progress in this session we have:

- Emoji checks
- Code-along
- Exercise in GCP

## Prep

- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises
- The instructor will need to make sure GCP individual account access is working ok (via console and CLI) to be able to complete the task in this session
- Make sure you are familiar with the code-along aspects of the session

## Session

- Run the presentation
- Make sure everyone keeps up with the code-along aspect of the session
- When it gets to the "Demo `one-to-one` Pub-Sub" then you can use the `solutions/gcp-07-pub-sub-session` folder as an example
    - The code is also at [JLR-DE-Academy/gcp-07-pub-sub-session](https://github.com/JLR-DE-Academy/gcp-07-pub-sub-session)
- When it gets to the exercise, depending on the cohort, you can show parts of the solution files if it helps them make progress
