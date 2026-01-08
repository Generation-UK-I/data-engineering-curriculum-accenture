## Terraform 101

This optional session is partly theory, and partly live demonstration. It is very basic in that it only goes as far as creating and then deleting a simple EC2 instance on AWS.

The theory parts should be deliverable pretty much using the content in `terraform.md` as is. This will also take the learners through setting up a simple `main.tf` file which we can then use to try out some terraform.

Steps on installing terraform are also included.

One point of friction can be ensuring terraform can access AWS using the access key and secret key. Depending on the method of AWS authentication used, it may be more tricky if the method does not utilise the `~/.aws/credentials` file - so put some thought in in advance of running the session ensure you can make this work.

## Overview

- What is infrastructure as code?
- What are the problems that it solves?
- What is terraform?
- Dive into some terraform

## Timings

- This session is timetabled for X blocks at 1.5 hrs each
- The formative assessments occur during this and are included in that timing
- The exercises for this session (done in breakouts) are also included in that time

## Assessments

TODO - list the formative assessments in the session - we need this for OFSTED etc:

To check the learner progress in this session we have:

- Quiz on X
- Discussion on Y
- Breakout on task Z
- etc

## Prep

- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises

## Session

- Run the presentation
