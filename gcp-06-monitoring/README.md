# Monitoring

This module introduces learners to the key components of monitoring.

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

- What does software monitoring consist of?
- Why do we monitor software?
- Monitoring infrastructure
- Monitoring applications

## Timings

- This session is timetabled for 2 blocks at 1.5 hrs each, i.e. 0.5 elapsed training days
- The formative assessments occur during this and are included in that timing
- The exercises for this session (done in breakouts) are also included in that time

## Assessments

To check the learner progress in this session we have:

- Quiz on X
- Discussion on Y
- Breakout on task Z
- etc

## Prep

- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises
- Export a copy of `exercises/monitoring-exercises.md` file as a PDF
- For the exercise, you will need to deploy the cloud function, this can be done manually or by running cloud sdk commands

## Session

- Give out the `exercises/monitoring-exercises.pdf` file you made above, or the `*.md` file
- Run the slide deck
- Give the learners some time to set up the docker instance for Grafana.
- Try and get all learners by the end of the lesson to have loaded up the Grafana dashboard and been able to create a new dashboard and panels
