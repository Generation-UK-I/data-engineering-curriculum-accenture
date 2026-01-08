# AWS (Combined session)

> Originally designed as a stand-alone session, subsumed into the AWS 01...10 sessions.

A very large continuous session on the parts of AWS that are core utilities, and essential for the final team projects.

The goal of the session is to show that if we break down AWS into the few services we need, and concentrate only on those, and only those we need for the project, then the scope is less than might be feared given the enormity of AWS.

This session is written in a different way to others:

- The descriptions of each service are intentionally brief, so as to not overwhelm the learners
- There is quite a lengthy exercise per service, so that the session is as hands-on as possible

Following sessions cover:

- [Data Warehousing inc. mention of Redshift](../data-warehousing/README.md)
- [Data Streams inc Kinesis](../data-streams/README.md)
- [OLD AWS intro + services](../aws/README.md)
- [OLD DevOps inc. CI](../devops/README.md)
- [OLD Cloudformation inc. CD](../cloudformation/README.md)

## Related documents

> Important! You will find these useful for reference:

- Main [../README.md](../README.md), `Final Project (second half of course)` section
- Main [../README.md](../README.md), `Related Documents` section for
    - Related repos
    - Team project documents!

## Overview

- What is AWS?
- AWS Console
- IAM
- AWS CLI
- EC2
- S3
- Lambda

## Timings

- This session is timetabled for 6 blocks at 1.5 hrs each, so 1.5 days
- The formative assessments occur during this and are included in that timing
- The exercises for this session (done in breakouts) are also included in that time

## Assessments

To check the learner progress in this session we have:

- Quizzes
- Discussions
- Breakout room exercises for each service
- Weekly Quiz on AWS topics

## Prep

- Create the session files (pdf and zip) using `make generate-session-files f=module_name` or `make gsf-local f=module_name`
- Review the slides and exercises
- This session is specifically aimed at AWS and should follow on after the "Intro to Cloud" external talk
- There are exercises throughout, ensure you are comfortable in completing them yourself first
- You should already have an AWS user setup for the account you will be using
- Ensure you have AWS CLI v2 installed and ensure you can use your profile for it

### Prep - required roles

Make sure you have run the commands for the AWS and project setup in advance:

- The instructions are here: [repo data-academy-final-project-infrastructure#commands-to-deploy](https://github.com/infinityworks/data-academy-final-project-infrastructure#commands-to-deploy)
- This creates the roles that you and the learners will need in this session and/or the next few weeks:
    - `lambda-execution-role`
    - `de-academy-ec2-role` and `de-academy-ec2-role-instance-profile`
    - `github-cicd-role`
    - `ScopePermissions` policy for use as a Permissions Boundary

### Prep - AWS console and CLI setup

Depending on the programme being delivered, share the appropriate `aws-setup-*.md` file with the cohort:

| Academy        | Setup File                 |
|----------------|----------------------------|
| Generation     | `aws-setup-sso.md`         |
| School of Tech | `aws-setup-azure-login.md` |

## Session

1. Run the slide deck
1. Have AWS console open and ready to use
1. For the exercises, if you use breakout rooms, it helps if there are regular check-ins maybe half way through each exercise back in the main room
