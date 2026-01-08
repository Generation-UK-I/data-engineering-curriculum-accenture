# Sainsburys Data Academy Programme Handbook

## Overview

The Sainsburys Data Academy programme is a 16 week data engineering programme designed for Sainsburys. Its intention is to help Sainsburys colleagues in non-technical roles change career and be ready to take on an entry level Data Engineer role within one of the Sainsburys data engineering teams.

The programme was originally developed for Sainsburys but run for the first time internally at IW (as Sainsburys initially postponed delivery of the programme due to the COVID-19 pandemic). It was based on the Python version of the IW internal Academy and has subsequently been evolved into a 12 week version which is delivered in partnership with the global employment charity [Generation](https://generation.org). Details of the Generation version can be found [here](../generation-data-academy/programme-generation-data-academy.md). Note the Sainsburys version contains additional content specific to Sainsburys, cross-references Sainsburys C3 level of their engineering framework and contains Sainsburys branding.

The mission of the programme is to ultimately get each learner ready for a [C3 entry level role](./sainsburys-c3-engineer.md) within the Sainsburys data engineering teams. Our key part of this at Infinity Works is to help them become well-rounded, adaptable Data Engineers that understand their role, responsibilities and ways of working. Also see the [Generation entry-level data engineer role](../generation-data-academy/data-engineer-role.md) for more details of a typical entry-level data engineer role.

## Programme structure

The 16-week course is split into two halves:

- Foundations & mini-project (weeks 1-7): introducing Python programming, CRUD data operations, simple data storage and basic application design from the ground up. This also includes introducing the learners to associated professional programming practices such as version control, unit testing, IDEs and the Unix shell. The majority of the time is spent delivering taught sessions and guided workshops, teaching learners the skills and concepts and practising these through exercises. In parallel the learners then apply these new skills and knowledge to a mini project, a simple CLI application which they build individually and which progresses incrementally over the six weeks. This helps them both solidify and apply learning and builds confidence in what they can achieve.
- Advanced Concepts & Final Project (weeks 8-16): building on the core skills learnt in the first half, the lessons now move on to focus more specifically around data engineering technologies, techniques and tools, together with agile delivery and cloud infrastructure. Concepts such as data normalisation, data encoding, data cleansing and ETL are introduced, together with data warehousing, data streaming and data queues. For the Sainsburys course Snowflake is also covered in a more comprehensive way. These are delivered via taught sessions but more time in the second half is also dedicated to working together in teams on a final team project with a shared codebase per team which builds up an ETL data pipeline to process, analyse and visualise data.
- Note Sainsburys effectively cover a week themselves, two days at the beginning of the programme and three days at the end.

## Course Content

### Timetable

The [Infinity Works Sainsburys Data Engineering timetable](https://docs.google.com/spreadsheets/d/1xLyo7PEReba1lNpp0iz32MYzbo_IIYtZG7x1w34RFps/edit) outlines the programme schedule. This visualises how the modules and project time below play out across the 16 week period.

### Programme narrative

The narrative provides a more cohesive story-based way to understand what the course is aiming to teach and deliver. That is, what is the purpose of what we're trying to teach, and what progression will the learner follow in order to gain their new skills and understanding? The narrative for this course is included as an [appendix](#appendix:-data-academy-supporting-narrative) at the end of this document.

### Modules

All of the course slides for technical modules are stored in the private GitHub repository [academy-curriculum](https://github.com/infinityworks/academy-curriculum). This is structured and setup as per the [Academy Handbook](https://docs.google.com/document/d/1wuyHMe7QYeG_6owbKvsGDgnJFjWuGTjIZ1Mr6JzlXn4/edit) and contains all the taught modules used across all the Academy programmes. This document outlines which of the modules are used in this specific programme and in which order they fall.

Note guest speaker slots aren't included in the repo or listed below; please refer to the timetable above to understand where these fall in the schedule.

#### Week 1

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| [Intro to programming #1](../../python-1.md) | 1.5 days |
| [VS Code tips and tricks](../../vscode-tips.md) | 0.25 days |
| [Intro to the mini project](../../mini-project.md) | 0.25 days |

#### Week 2

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| [Intro to programming #2](../../python-2.md) | 1.5 days |
| [Unix shell](../../unix-shell.md) | 0.5 days |
| [Data persistence](../../data-persistence.md) | 0.75 days |

#### Week 3

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| [The Python ecosystem](../../python-ecosystem.md) | 0.75 days |
| Unit testing I | 0.75 days |
| [Data encoding](../../data-encoding.md) | 0.75 days |
| [Working in a team](../../working-in-team.md) | 0.5 days |

#### Week 4

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| [Programming standard practices](../../programming-practises.md) | 0.5 days |
| [Source control](../../source-control.md) | 0.75 days |
| Unit testing II | 0.75 days |
| Object-oriented programming | 1 day |

#### Week 5

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| Unit testing III | 0.5 days |
| [Databases](../../databases.md) | 2.5 days |

#### Week 6

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| Functional testing | 0.5 days |
| Introduction to visualisation | 1 day |
| [APIs](../../APIs.md) | 0.5 days |

#### Week 7

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| Docker | 1 day |
| [Shell scripting](../../shell-scripting.md) | 0.5 days |

#### Week 8

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| _Agile and project inception week - all guest speaker content_ | n/a |

#### Week 9

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| Data normalisation | 0.75 days |
| ETL/ELT | 0.5 days |
| Data cleansing | 0.5 days |

#### Week 10

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| _No taught content at present - Final project time_ | n/a |

#### Week 11

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| AWS | 1.5 days |
| Data warehousing | 0.5 days |

#### Week 12

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| Continuous integration and delivery | 0.5 days |
| Data Lakes | 0.25 days |
| Monitoring | 0.5 days |

#### Week 13

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
 _Snowflake week - all guest speaker content_ | n/a |

#### Week 14

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| Queues | 0.5 days |
| Data streams | 0.5 days |

#### Week 15

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| _No taught content at present - Final project time_ | n/a |

#### Week 16

| Lesson        | Approx delivery length |
| ------------- | ---------------------- |
| _No taught content at present - Sainsburys wrap-up_ | n/a |

## Projects

### Mini project (Weeks 1-7)

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

### Final project (weeks 7-12)

TODO - Add in details of the final project

#### Final project Data Producer setup

TODO - Add in details of the Data producer and it's setup

## Hosting

Sainsburys are providing brand new MacBooks for all learners so we can assume Mac OSX and high spec machines.

Learners should set up their machines as per [Setting up your machine](https://docs.google.com/document/d/17ih3szcsPbPCdBuyt02ZLG7rG53P-CPoZGtJM5aX6nc/edit).

### Github setup

Infinity Works provide the technical setup of Github in order to support the programme. A public organisation is used to both house all the learners' individual mini project repos for the mini-project (which makes for ease of instructor access) and also for the team repos for the final project. How to set this up is outlined in this Google doc [How to configure Github for programme learners](https://docs.google.com/document/d/1J76rK1SXBoxeduKh4HBRXFMvTmu_jwLI-Nfg6GE_HGM/edit).

### AWS

Infinity Works also provide the AWS accounts, access and admin in order to allow the learners to build their final projects on the AWS cloud and using AWS tools such as Lambda, EC2, Redshift and Kinesis. This must be carefully set up and managed to avoid the very real security risk that comes from learners using AWS under Infinity Works accounts.

TODO: Add in AWS set up details here

## Points of contact

| Name | Role | Can Help With... |
| ---- | ---- | ---------------- |
| Clem Pickering | Director of Academy | General enquiries, programme and Academy information |
| Colin Scally | Academy Lead - Technical | Programme info, technical queries |
| Ruari Armstrong | Academy Lead - Technical | Programme info, technical queries |
| Sam Evans | Academy Lead - Technical | Programme info, technical queries |
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

**Data Visualisation:** Up to this point things have been quite dry and low-level, as we've only been working with raw data. It'd be insightful to somehow plot out the data we've been working with in our DB so we can visualise it, as a graph or in some human-friendly way. Perhaps we'll be able to surface interesting qualities in it that we couldn't see before. How do we look at stuff that our application has consumed? Yeah sure, looking at string representations of those is pretty cool, we devs understand and can find that useful. It lets us search things easily, maybe even run a fun script that gives us another useful output - some other values that tell us something about the data we've got. Okay, that's really powerful, but what if we want to _really see_ the trends? Graphs? Definitely, they can look cool, people grasp more from diagrams than they do from words (sometimes) and it means that we can show these to people that maybe don't care about the words. So, we want to visualise this, what's the minimum amount of work we can put in to get something that looks cool on the screen? matplotlib! Okay, how easy is it to get started with and how powerful can those graphs and other visualisations look? Pretty complex, actually. With some experience it's a powerful tool to wield and gives us more of an insight into the data we're consuming. So, matplotlib is really useful, but maybe there are some usability downsides to it, maybe we don't want to be doing those visualisations through that but through a tool that gives us more flexibility for everything else we're going to be using… Enter, Jupyter Notebooks ...

**APIs:** So far we've been getting our data from pre-existing files or manually from the user. But that's not terribly useful. New data is produced all the time. It's got to be available somewhere! Cue in, API services

**Bash:** Standing up our infrastructure is annoying and painstaking. This is one of the many tasks we could automate with Bash scripting.

**Docker:** Running our own SQL DB in our laptop without having to mess around with packages and local DB server would be useful. It'd also be great to have a way to bundle up our software into a self-contained package that works exactly the same way no matter where it runs. This would make deploying our software to a remote server much easier.

**The Cloud:** The kind of volumes of data that companies manipulate in the real world is way, way larger than a few MB/GBs. Let's get a taster of that. Turns out though, we can't fit a 5TB file in our puny little laptops. Even if we could, we couldn't possibly process it, as it would take ages. So we need bigger hard drives and more powerful computers! But where do we get that from?

**Monitoring:** There are so many changes happening with our application that we need a dashboard just to know what's going on.  We need to determine what to track in the terms of business and application metrics, then we need to show what's happening in a timely manner!

**Data Store Scalability:** Let's all hit our single DB server with a ton of expensive queries. What do you think will happen? It will go down, or at the very least, become overloaded and perform very poorly. This is a situation bigger companies in the real world deal with on a daily basis, as their data processing needs grow.

**Big Data/DWH/Redshift:** Storing data in RDS means we have access to massive hard disks and can request powerful DB servers that can handle our queries. It looks like now we're in a good place to start extracting useful information from data. Ok, let's try with that 5TB file we were speaking about before, shall we? Turns out, performance is nowhere near where it needs to be, and it would be really pricey to scale up our DB to handle this kind of workload regularly. Isn't there a better way to do this? Maybe a type of DB which is optimised for storing large amounts of data and then interrogating it? With Redshift, we now have a specialised, big-data-optimised OLAP DB that will fulfil our storage and data interrogation needs.

**Data Security:** The data we've been working with so far has contained all sorts of things, including PII and other sensitive information. Oh, no! We're in big trouble if we don't sort this, as not only is it mandated by company policy but also it's regulated by the law. Scare them with stories of big data leaks that have caused massive financial and reputational damage to institutions and companies.

**Data Cleansing:** We've been getting tons of data and can now process it fairly efficiently upon ingestion, but the data is often of poor quality, which hampers our ability to gain useful insights from it, as there's loads of noise which makes processing the data more difficult, brittle and produces clouded outputs at best.

**ETL:** We can manually insert data into Redshift or work with data that is already there, but what about importing data of our own? There are some modifications or enriching we need to do on the data, but at the moment it's not really plausible. We have to modify the source dataset if we want to have that. How about doing this in an automatic, repeatable manner? At the moment we're sort of manually getting data in our bespoke app to be processed and stored in a DB. Or maybe we're running some queries manually to process and transform the data. This is not good as bespoke, monolithic applications will only get us so far. How can we automate this process and make it able to sustain large, continuous data intakes?

**Serverless:** Redshift is great in dealing with our big data needs but they're a pain to manage, we have to worry about whether we've got enough capacity provisioned to handle our ever-growing workloads, and we don't like maintaining them all the time.

**Queues:** The data we're receiving is getting even larger and our lambdas are timing out or erroring out because they're reaching their limits in terms of runtime and concurrency (thousands of files could be uploaded any minute). There's no way for us to detect this and recover from it, retry, etc. This is not a robust process. Furthermore, we keep getting asked to incorporate new, different data sources into our data pipelines. Wiring all of this together is very hard!

**CI/CD:** Every time we make a change to our system we need to manually test everything and make sure we didn't introduce any regressions. Also, sometimes we introduce pretty obvious faults in our code and config and we know there are ways to catch these issues (e.g. linters, YAML/TF validation steps), but we forget to run these ourselves most of the time. Further to this, our deployment processes and Terraform `apply`'s are quite mechanical, involve a series of manual checks and steps to be done and there's the potential we end up running the wrong command (or running a command against the wrong environment) and messing things up.

**Data Lakes:** What happens when we go even bigger than a few TBs? We've been producing data at a large scale for a large amount of time now and things like Hadoop and EMR are not cutting it anymore, not to mention they're quite expensive, complex to set up and maintain, and it's not efficient to be writing data to them constantly.

**Data Streams:** So far, our data ingestion mechanism has been fairly slow, manual and asynchronous. But we need to get the information ASAP. The sooner the better, especially because if we let our systems sit for too long, soaking in swathes of data, it could take ages to process it all. Some people actually do this, it's called batch processing. And it may be OK, but sometimes you need to extract information as it is produced, rather than having to wait minutes or even hours. Data streams allow you to consume and process data almost in real-time. Another issue is that our data batches are pretty big and we don't have a nice, easy way to chunk them up into lumps that can be readily processed by our pipeline. This is making our lives pretty difficult as we can't really work with large datasets like this (micro-batching).

![Narrative Flow](../../img/narrative.png)
