# DevOps

> Originally designed as a stand-alone session, subsumed into the AWS 01...10 sessions.

This module introduces learners to the concept of DevOps, which is a set of practices that combines software development (Dev) and IT operations (Ops).

We introduce learners to the overall concept of DevOps and it's philosophies. CI/CD is the main topic covered.

Related sessions cover:

- [Data Warehousing inc. mention of Redshift](../data-warehousing/README.md)
- [Data Streams inc Kinesis](../data-streams/README.md)
- [OLD AWS intro + services](../aws-combined-old/README.md)
- [OLD DevOps inc. CI](../devops/README.md)
- [OLD Cloudformation inc. CD](../cloudformation/README.md)

## Overview

- Introduction to DevOps
- Continuous Integration / Continuous Delivery (CI/CD)

> Note that Continuous Integration (CI) and Continuous Deployment (CD) separate sessions are not specifically in the Data Engineering shorter courses by default.

## Timings

- This session is timetabled for 1 block at 1.5 hrs each, i.e. 0.25 elapsed training days
- The formative assessments occur during this and are included in that timing
- The exercises for this session (done in breakouts) are also included in that time

## Assessments

To check the learner progress in this session we have:

- Quizzes on CI and CD
- Emoji Checks
- Breakouts to create a CI/CD pipeline

## Prep

- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises
- Make sure the federated logon from GitHub to AWS has been set up - see [data-academy-final-project-infrastructure](https://github.com/infinityworks/data-academy-final-project-infrastructure) and the `github-cicd-role` role in the `cohort-iam-roles` stack
    - There is an example of the use of this in the [data-academy-final-project-example](https://github.com/infinityworks/data-academy-final-project-example)
    - This is used in the CloudFormation session, not this one, but that is usually the next day, so now is a good time to check :-)

### For this module

- Review the slides and be comfortable yourself in the proponents of DevOps.
- Examine the CI/CD example workflow and decide which repo you will use for demonstration to the learners (can be any repo as long as there are files in it!)

### Post-module:

After this module, learners will later go on to implement CI/CD as part of their final project.

- See the main repo [../README.md](../README.md) and the `Related Documents` section for details of the Team Project documentation.

## Session

- Run the presentation
- Demonstrate example workflow
- Distribute exercise - when doing the breakouts remind the learners to all do this so to each try it in their mini-project repos
