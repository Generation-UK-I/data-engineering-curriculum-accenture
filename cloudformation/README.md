# CloudFormation (Old)

> Originally designed as a stand-alone session, now deprecated

This module is intended to teach the fundamentals of cloudformation, including how to create and update stacks with the AWS CLI.

Live demonstrations of the concepts in the lesson by instructors is very helpful to learner understanding.

The material in the module is supplemented by exercises which follow a very similar format to reinforce the learning.

The exercises will take learners **a significant amount of time to complete** however it is suggested that learners be given a good amount of time on these, as the lessons will arm learners with most of the fundamental building blocks they need to move their final project into the cloud.

Related sessions cover:

- [Data Warehousing inc. mention of Redshift](../data-warehousing/README.md)
- [Data Streams inc Kinesis](../data-streams/README.md)
- [OLD AWS intro + services](../aws-combined-old/README.md)
- [OLD DevOps inc. CI](../devops/README.md)
- [OLD Cloudformation inc. CD](../cloudformation/README.md)

## Overview

- Infrastructure as Code
- CloudFormation concepts
- CloudFormation Syntax and Features
- Deploying CloudFormation to AWS
- Troubleshooting CloudFormation
- Exercise

## Timings

- This session is timetabled for 3 blocks at 1.5 hrs each, or 0.75 day.
- The formative assessments occur during this and are included in that timing
- The exercises for this session (done in breakouts) are also included in that time

## Assessments

To check the learner progress in this session we have:

- Quizzes on CF
- Breakouts on using CF
- Emoji checks

## Prep

- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises
- Ensure functional AWS CLI
- Ensure the AWS account to be used for demo has a Default VPC - this is required for the EC2 template deployment
- Make sure the federated logon from GitHub to AWS has been set up - see [data-academy-final-project-infrastructure](https://github.com/infinityworks/data-academy-final-project-infrastructure) and the `github-cicd-role` role in the `cohort-iam-roles` stack
    - There is an example of the use of this in the [data-academy-final-project-example](https://github.com/infinityworks/data-academy-final-project-example)

## Session

- Run the presentation
