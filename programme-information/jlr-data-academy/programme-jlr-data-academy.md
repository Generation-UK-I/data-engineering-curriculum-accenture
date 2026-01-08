# Jaguar Land Rover Data Academy Programme Handbook

## Overview

The Jaguar Land Rover Data Engineering programme is intended to take a cohort of 12 Jaguar Land Rover (JLR) staff who are internally re-skilling from other roles within the organisation into Data Engineering. The course will support people from all backgrounds and does not assume prior experience.

The mission of the programme is to furnish each learner with the skills necessary to assume an entry-level data engineer position within JLR.

## Programme structure

The course is intended to run over 7-8 months of elapsed calendar time, and is split into two parts:

- Foundations & mini-project (Full-time instruction, Weeks 1-6): introducing Python programming, CRUD data operations, simple data storage and basic application design from the ground up. This also includes introducing the learners to associated professional programming practices such as version control, unit testing, IDEs and the Unix shell. The majority of the time is spent delivering taught sessions and guided workshops, teaching learners the skills and concepts and practising these through exercises. In parallel the learners then apply these new skills and knowledge to a mini project, a simple CLI application which they build individually and which progresses incrementally over the six weeks. This helps them both solidify and apply learning and builds confidence in what they can achieve.
- Advanced Concepts & JLR project: (2-3 days of engagement per month over the following 6 months)

## Course Content

### Timetable

The [JLR timetable](https://docs.google.com/spreadsheets/d/14zZafyI6BjyfiIDL_D8Bh7bIbkr9JnJnAz7FEbspESk/edit#gid=840254940) outlines the programme schedule.

### Programme narrative

The narrative provides a more cohesive story-based way to understand what the course is aiming to teach and deliver. That is, what is the purpose of what we're trying to teach, and what progression will the learner follow in order to gain their new skills and understanding? The narrative for this course is included as an [appendix](#appendix:-data-academy-supporting-narrative) at the end of this document.

### Modules

All of the course slides for technical modules are stored in the private GitHub repository [academy-curriculum](https://github.com/infinityworks/academy-curriculum). This is structured and setup as per the [Academy Handbook](https://handbook.infinityworks.com/academy) and contains all the taught modules used across all the Academy programmes. This document outlines which of the modules are used in this specific programme and in which order they fall.

#### Week 1

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| [VS Code tips and tricks](../../vscode-tips.md) | 0.25 days |
| [Intro to programming #1](../../python-1.md) | 1.5 days |
| [Intro to programming #2](../../python-2.md) | 0.75 days |

#### Week 2

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| [Intro to programming #2 (continued)](../../python-2.md) | 1.25 days |
| [Unix shell](../../unix-shell.md) | 0.5 days |
| [The Python ecosystem](../../python-ecosystem.md) | 0.75 days |
| [Data persistence](../../data-persistence.md) | 0.5 days |
| [Programming standard practices](../../programming-practises.md) | 0.5 days |

#### Week 3

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| [Data encoding](../../data-encoding.md) | 0.75 days |
| Unit testing I | 0.75 days |
| [Source control](../../source-control.md) | 0.75 days |

#### Week 4

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| Unit testing II | 0.75 days |
| Working in a Team | 0.5 days |
| Object-oriented programming | 0.75 days |
| Unit testing III | 0.75 days |

#### Week 5

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| Docker | 0.6 days |
| [Databases](../../databases.md) | 2.5 days |

#### Week 6

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| Functional Testing | 0.5 days |
| [Shell scripting](../../shell-scripting.md) | 0.25 days |
| Data Visualisation | 0.75 days |
| [APIs](../../APIs.md) | 0.5 days |
| Data Normalisation | 0.5 days |

## Projects

### Mini project (Weeks 1-6)

In order to support and reinforce the concepts introduced in the first half of the course with hands-on experience, an individual, 6-week _miniproject_ is followed, where the learners are required to develop a CLI application in the default programming language for the course, **Python 3**. The premise or theme for the mini project is that of a pop-up café that delivers food and refreshments, and requires an app to track orders, delivery couriers and products. Details can be found [here](../../mini-project.md).

The learners are expected to incrementally improve their application by applying new techniques and tools as they're introduced to them, thus evolving it from a simple command-line application to a fully-featured data producing and analysing application.

In order to provide a general direction and goals, the learners are given a list of feature requirements to implement every week, with the idea that these will allow them to practice what they've learned that week.

The miniproject requirements are incorporated into the weekly core goals documents, which contain a list of all the goals the learners should aim to complete by the end of the week. In order to ensure everyone has a chance to complete the coursework, regardless of their skill level, the goal list is divided into three difficulty tiers.

- Core goals: these goals are the bare minimum required to attain the key learning objectives for the week and progress the miniproject to a point where it'll be possible to complete the core goals of the following week.
- Stretch goals: optional goals of harder difficulty meant for people who have completed all of the core goals. The completion of the stretch goals is not indispensable to progress with the course or achieve the core requirements of the miniproject but provide an extra challenge for those who seek to learn more.
- Bonus stretch goals: optional goals of even higher complexity geared towards people with a decent amount of coding experience (or a lot of time in their hands). These may require independent research of tools and notions possibly beyond the scope of the course.

| Weekly goals |
| ------------ |
| [Week 1 goals](../../mini-project/breakdown/WK1.md) |
| [Week 2 goals](../../mini-project/breakdown/WK2.md) |
| [Week 3 goals](../../mini-project/breakdown/WK3.md) |
| [Week 4 goals](../../mini-project/breakdown/WK4.md) |
| [Week 5 goals](../../mini-project/breakdown/WK5.md) |
| [Week 6 goals](../../mini-project/breakdown/WK6.md) |

### JLR project (weeks 7+)

TODO - Add in details of the final project

### Github Setup

Infinity Works provide the technical setup of Github in order to support the programme. A public organisation is used to both house all the learners' individual mini project repos for the mini-project (which makes for ease of instructor access) and also for the team repos for the final project. How to set this up is outlined in this Google doc [How to configure Github for programme learners](https://docs.google.com/document/d/1J76rK1SXBoxeduKh4HBRXFMvTmu_jwLI-Nfg6GE_HGM/edit).

## Points of contact

| Name | Role | Can Help With... |
| ---- | ---- | ---------------- |
| Clem Pickering | Director of Academy | General enquiries, programme and Academy information |
| Tim Slow | IW IT Systems Manager | Top level AWS setup and Github access |

## Appendix: Data academy supporting narrative

**The Narrative:** What's the story behind why we need to understand these concepts and topics? What is the purpose of what we're trying to learn? What problem is it solving for us right now? Note this doesn't necessarily tie in exactly with the order the course is delivered.

**Theme: Information:** That is the goal, to build systems that allow us to collect and process data so that we can extract the most valuable information we can.

**Define the Problem:** We live in the era of Information. More information is captured and shared than ever before. This information allows us to make better decisions, and it also enables businesses to make decisions and predict outcomes like they've never done before. The problem is, information is rarely that obvious. It needs to be surfaced.

**What is Data:** Think of data as a "raw material" - it needs to be processed before it can be turned into something useful. Hence the need for "data processing". Data comes in many forms - numbers, words, symbols. Data relates to, for example,  transactions, events and facts. On its own - it is not very useful.

**What is Information:** Information is data that has been _processed_ in such a way as to be _meaningful_ to the person who receives it. Note the two words highlighted in italics - "processed" and "meaningful". It is not enough for data simply to be processed. it has to be of use to someone - otherwise why bother?

**Producing data:** Hardcoded values in a program.
    - But data is rarely static, it changes.

**Taking user input:** now we work with dynamic data but when we shut down the program, it disappears. How do we fix that?

**Storing data to a file and recovering it:** The file won't scale much and it's quite cumbersome to save and recover data in an efficient, structured manner.

**OOP:** Writing our application as a series of functions and variables has only got us so far. Our code is starting to become a bit messy and it's getting harder to see what belongs where.

**Data encoding:** We can encode our data in certain ways to make it easier to save and recover: CSV, XML, JSON...

**Unix CLI:** Automation at your fingertips. First foray into data pipelines, i.e. shell pipes, redirecting output to files, text processing tools, etc.

**Testing:** Our data handling apps have been getting increasingly complex, as has our data. Every time requirements change or we add new ways to process it, we need to manually feed our application 10 different data sets to ensure we haven't broken anything.
    - How do we make sure our data collection and processing is right?

**Source Control and Writing Modular Code:** Our code is getting relatively complex and big by now which means understanding, changing and expanding is getting increasingly harder. Also, if we wanted to share code with others or reuse code written by our peers, we'd have to have it sent by them to us and then to copy-paste it into our project. Not to mention if we mess anything up in our code, there may be a fair amount of rewriting to be done to fix it!

**Databases:** We've been working with plaintext files so far. Even though saving data as CSV or JSON gets around the issue of storing relatively complex data effectively, now we need to think about the relationships between our data, and also the volume of our data.
    - What if someone else wants to access or change this data?

**Data Visualisation:** Up to this point things have been quite dry and low-level, as we've only been working with raw data. It'd be insightful to somehow plot out the data we've been working with in our DB so we can visualise it, as a graph or in some human-friendly way. Perhaps we'll be able to surface interesting qualities in it that we couldn't see before. How do we look at stuff that our application has consumed? Yeah sure, looking at string representations of those is pretty cool, we devs understand and can find that useful. It lets us search things easily, maybe even run a fun script that gives us another useful output - some other values that tell us something about the data we've got. Okay, that's really powerful, but what if we want to _really see_ the trends? Graphs? Definitely, they can look cool, people grasp more from diagrams than they do from words (sometimes) and it means that we can show these to people that maybe don't care about the words. So, we want to visualise this, what's the minimum amount of work we can put in to get something that looks cool on the screen? matplotlib! Okay, how easy is it to get started with and how powerful can those graphs and other visualisations look? Pretty complex, actually. With some experience it's a powerful tool to wield and gives us more of an insight into the data we're consuming. So, matplotlib is really useful, but maybe there are some usability downsides to it, maybe we don't want to be doing those visualisations through that but through a tool that gives us more flexibility for everything else we're going to be using... Enter, Jupyter Notebooks ...

**APIs:** So far we've been getting our data from pre-existing files or manually from the user. But that's not terribly useful. New data is produced all the time. It's got to be available somewhere! Cue in, API services

**Bash:** Standing up our infrastructure is annoying and painstaking. This is one of the many tasks we could automate with Bash scripting.

**Docker:** Running our own SQL DB in our laptop without having to mess around with packages and local DB server would be useful. It'd also be great to have a way to bundle up our software into a self-contained package that works exactly the same way no matter where it runs. This would make deploying our software to a remote server much easier.

![Narrative Flow](../../img/narrative.png)
