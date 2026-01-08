# Data Academy Curriculum (Python)

This repository contains all of the technical curriculum resources used as part of any School of Tech Data Engineering Academy programme in Python. There are modules for AWS (with Cloud Formation) and GCP.

Each academy programme is defined in the [programme-information](./programme-information/) directory, containing documentation relevant to each course.

For further information please contact the [School Of Tech team](https://github.com/orgs/infinityworks/teams/academy-leads).

## Technical Repository Setup

For details see [GitHub Repo Management For Technical Courses.docx](https://ts.accenture.com/:w:/r/sites/AccentureSoTFY24/Shared%20Documents/General/Runbooks%20for%20technical%20management/GitHub%20Repo%20Management%20For%20Technical%20Courses.docx?d=w716396733a024470a2dae9c89b4a923d&csf=1&web=1&e=oMNjhl) in [Accenture SoT | Files | Runbooks for technical management](https://ts.accenture.com/:f:/r/sites/AccentureSoTFY24/Shared%20Documents/General/Runbooks%20for%20technical%20management?csf=1&web=1&e=p6SW1I).

Also please direct any queries to the [code owners](./.github/CODEOWNERS).

## Overview

We deliver 7, 9 and 12 week courses for Accenture and our clients, e.g. [Generation.org](https://www.generation.org/). This repository is for the Data Engineering courses - we also run Full Stack, Tech Transformation and Product Academy training.

The whole course is full time and Instructor lead, and while teaching the fundamentals we also cover a Mini Project in the first half and a team project in the second half.

### Mini Project (first half of course)

In the first half of the course the learners do a [mini-project](./mini-project). See that directory for details - it is a command line Coffee Orders app that builds up over the weeks, in a solo project.

On 7 week courses we drop this due to time constraints.

### Final Project (second half of course)

We divide the cohort into teams for the final half of the course, and they build an ETL pipeline in AWS (or GCP) which consumes dummy data the Coffee Orders apps may have sent.

We have an extensive document  - this is the source of truth on the final project implementation. Copies are in:

- In Teams for SoT: [DE Final Project word doc](https://ts.accenture.com/:w:/r/sites/AccentureSoTFY24/Shared%20Documents/General/NGE%20Material/Data%20Engineering%20Academy%20-%20Common/DE%20Final%20project.docx?d=wb8ea5df5722b4647889cb62907717c8f&csf=1&web=1&e=L5Ln9D)
- In GDrive for Generation: [DE Final Project google doc](https://docs.google.com/document/d/1GQ6avVo6iwYYs3LC7qPPmIIszPKaMyenuO8VvMjk2yM/edit#)

The is a presentation to introduce the final project, as well as documentation on what to know as an instructor;

- In the [final-project-7-week-sot](./final-project-7-week-sot) folder for SoT
- In the [final-project](./final-project) folder for Generation

## Instructors Setup

For new instructors joining the Academy there is a wealth of material for setting the Academy and yourself up as well as information on how the Academy runs.

## Contributing: Writing RevealJS Slides and Sessions

For guidance on editing existing sessions, making new sessions, linting and code snippet imports and so on, please see the [README-06-contributing-to-sessions.md](academy-presentation-tooling/README-03-contributing-to-sessions.md) file.

### Course Setup

There are many peripheral setup jobs such as Slack channels, Teams that are required for the Academy to function smoothly. These are detailed in [Academy Course Setup](README-03-curriculum-specific-course-setup.md).

### Technical Setup

To get your laptop set up for running the Academy sessions and in particular using RevealJS there are a few tasks to complete which can be found in [Instructor technical setup](README-01-technical-setup.md). This includes the technical setup the Academites will also have to complete.

See the readme on [Instructors Pre-Course setup](academy-presentation-tooling/README-01-using-revealjs.md) to do your technical setup of the Instructors IDE and files before presenting.

## Onboarding

Starting with explaining through the timetable will enable an overall view of the course, from which the instructors can split off and discuss individual sessions in more detail. This also enables everyone to see room for improvements, tweaks and any new material. For further details see the [Instructor Onboarding google drive folder](https://drive.google.com/drive/u/0/folders/1KblIfpNj04diw5PJ-yLZn2KopJiPTs37).

## Directory structure

Each presentation consists of a single markdown file at the root level. Accompanying content lives in a directory with the same name. Sub-directories organize this content. See [README-03-contributing-to-sessions.md](academy-presentation-tooling/README-03-contributing-to-sessions.md) for more details.

## The `misc` folder

Has other related useful documents;

- `daily-open-and-close` suggestions for Instructors on how you might structure the ends of the day
- `learner-survey` sample survey for the end of the course
- `optional-sessions` extra ad-hoc session ideas for advanced students or refresher sessions
- `social-ideas` for more ice-breaker suggestions
    - `get-to-know-you-quiz`
    - `hackathons`
    - `two-truths-and-a-lie`

### Related documents

- [academy-core-infra repo](https://github.com/infinityworks/academy-core-infra) - all the core AWS infrastructure for SoT courses
    - We are gradually porting over all the items from [data-academy-final-project-infrastructure repo](https://github.com/infinityworks/data-academy-final-project-infrastructure) which is mainly for Generation
- [data-academy-final-project-infrastructure repo](https://github.com/infinityworks/data-academy-final-project-infrastructure) - shared infra to run the final projects in
- [data-academy-cafe-data-producer repo](https://github.com/infinityworks/data-academy-cafe-data-producer) - a utility app that generates the dummy data required for the teams to ingest for the final projects
- [data-academy-final-project-boards repo](https://github.com/infinityworks/data-academy-final-project-boards) - processes and scripts for managing final project sprint boards on the DE academy
- [data-academy-pipeline-example repo](https://github.com/infinityworks/data-academy-pipeline-example)
    - This one includes all CF, sample lambda ETL and db-connection code, etc
- [data-academy-minetest-cloudformation repo](https://github.com/infinityworks/data-academy-minetest-cloudformation) - For Generation, run Minetest for Agile Day from here
- Generation AWS Management with Control Tower - how we setup and organise the AWS accounts
    - [Teams Word doc](https://ts.accenture.com/:w:/r/sites/AccentureSoTFY24/Shared%20Documents/General/NGE%20Material/Data%20Engineering%20Academy%20-%20Common/Generation%20AWS%20Management%20with%20Control%20Tower.docx?d=wecb704037bce4f8d95175f7c02ccad33&csf=1&web=1&e=IwbF4V)
    - [GDrive google doc](https://docs.google.com/document/d/10xv8hl_bPzx8r6rQPt6p9NLYt_9zNHkk1ixdVhKyDXY/edit#heading=h.vxoa2rmlwyzp)
- DE Final project doc - all about the final team project
    - [DE Final Project word doc in Teams](https://ts.accenture.com/:w:/r/sites/AccentureSoTFY24/Shared%20Documents/General/NGE%20Material/Data%20Engineering%20Academy%20-%20Common/DE%20Final%20project.docx?d=wb8ea5df5722b4647889cb62907717c8f&csf=1&web=1&e=L5Ln9D) in Teams for SoT
    - [DE Final Project google doc in GDrive](https://docs.google.com/document/d/1GQ6avVo6iwYYs3LC7qPPmIIszPKaMyenuO8VvMjk2yM/edit#) in GDrive for Generation
