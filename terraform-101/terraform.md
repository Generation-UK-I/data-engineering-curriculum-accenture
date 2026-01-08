---
title: Terraform
---

## Terraform

---

## Overview

- What is infrastructure as code?
- What are the problems that it solves?
- What is terraform?
- Dive into some terraform

---

## Learning Objectives

- See some HCL (HashiCorp Configuration Language)
- Writing some HCL
- Use Terraform in AWS

---

## Infrastructure as Code

- The purpose of infrastructure as code is that you are able to **manage** your **cloud infrastructure** using **configuration files**
- By writing infrastructure as code, we write the configuration files, then use **some tool** to **deploy** our infrastructure
- This technology will interface with AWS, and **interpret** what we've written, and then **build our infrastructure** based on this

---

## What did infrastructure provisioning look like...?

- Let's look at the bad old days. Let's say you need some infra to run a new application - which also requires a database. You would have to:
    - Order your server and database server. Then wait for them to arrive
    - Provision them yourself - get them to a server room / data centre, sort out power, networking etc
    - Get all of the underlying software etc set up
    - Worry about what to do if there's too much load - do we buy spare or redundant servers too?

---

## Enter cloud computing...

- Then came cloud computing
    - We hand all of the above over to a cloud provider, like AWS, who does all those boring tasks
    - Want a new server? Log in, click a few buttons, you get a new server.
    - AWS can auto-scale your infra as well, so you don't have to worry about that either.

- But, not every problem is solved.....!

---

## Enter cloud computing...

- Let's say we're working for a big company - how do we keep track of all the things people have been building in AWS...?
- How do we enforce some consistent standards across what people are building?
- Can we do better at preventing unintentional issues where people create/delete infra?
- If things do go wrong, how can we roll back consistently and rationally...?
- How do we avoid 'forgotten' infrastructure being left about, costing us money?

---

## Infrastructure as Code

These are the types of problems that Infrastructure as Code can solve for us!

Building your infra using IaC should result in the same outcome as clicking around in the console, but it is a much better way of **managing** the build process!

---

## Infrastructure as Code - Benefits...

1. Single source of truth for your whole infrastructure
1. Easier to bring consistency (if you need a new server, you can often 'copy and paste' an existing one)
1. Version control! Can put your infra into GitHub for collaborative working, and to be able to redeploy from history if it goes wrong
1. State management - intelligently update your overall infrastructure only with changes

---

## The parts involved

- Your configuration files - often something like yaml
- The tool which interprets it (e.g. Terraform)
- The cloud provider (a.g. AWS)

**Write** the code in config files, **deploy** it using the interpreter tool, **build** it in your cloud provider!

---

## So what does Terraform actually do?

- It reads and interprets the config files you write which define all the bits of infrastructure you want
- It stores a state file - this is all the current bits of infrastructure that exists
- It recognises the gaps and creates a 'plan' that will show what will be added/changed/removed
- It interfaces with AWS to execute those changes

---

## What technologies are out there

- CloudFormation - an AWS service. Very much 'baked in' to AWS.
    - Great if you're using AWS services only
    - AWS managed service, makes it a little easier to use and get support
    - Automatic state storage
- Terraform
    - Not tied to AWS - can use for Microsoft Azure, GCP etc
    - Ironically, often supports new AWS services quicker than CloudFormation
    - Slight management required for state storage
    - More flexible and modular

Are there others out there? Yes
Are we going to talk about them? No

---

## Let's start terraforming!

First step - install terraform

```sh
brew tap hashicorp/tap
```

```sh
brew install hashicorp/tap/terraform
```

```sh
terraform --version
```

---

## Create a terraform file

- Make a new directory somewhere. Inside that directory, create a file called `main.tf`
- Open this file in VSCode (you might get a message about installing a plugin - go for it!)

---

## Create a terraform file

We will start building up a terraform file...

```terraform
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
}
```

---

## Create a terraform file

This first block is mainly some settings, and should just be needed once per project

In a minute it will allow terraform to download an aws plugin which it will then use

---

## Create a terraform file

- Next block, paste this below the last one. Change `default` to the name of the profile you use for aws

```terraform
provider "aws" {
  profile = "default"
  region  = "eu-west-1"
}
```

---

## Create a terraform file

This second block is for configuring terraform so it can access our AWS account.

It will use your profile to get an access key and secret for aws so it can 'log in' and do stuff

---

## Create a terraform file

- Final block, paste this below the last one. Change `ec2_tf_colin` to something else

```terraform
variable "name"{
  type = string
}

resource "aws_instance" "ec2_tf" {
  ami             = "ami-079d9017cb651564d"
  instance_type   = "t2.micro"
  subnet_id       = "subnet-0ff1cb53985c9103f"

  tags = {
    Name = var.name
  }
}
```

---

## Create a terraform file

This third block is where we actually start to say what we want to build!

Here we say we want an ec2 instance, and give it some configuration (AMI, instance type etc)

---

## Initialise...

run `terraform init` in your command line

This is actually going to set up terraform by downloading and setting up the provider we've defined, configuring it with our aws keys etc.

Essentially it gets the terraform tool ready to connect to our AWS and do stuff

---

## Format...

Optionally, run `terraform fmt`

It just enforces a standardised format so everything is easier to read. Not much value in a file like ours, but you get large projects with multiple terraform files, and this becomes quite handy

---

## Validate...

Optionally again, run `terraform validate`

This checks you haven't made mistakes etc...

---

## Plan

We'll need to do some login first....

Next, run `terraform plan`

This will check what's in your code, versus what's in Terraform's stored state - the record of existing infrastructure. It will then show you exactly what will happen when you deploy...

Technically optional, but I would always recommend it...!

---

## Apply

The final step is to run `terraform apply`

This is going to actually build your ec2 instance.

We can browse in the console and find it.

---

## State

Terraform cares about **state** - after you applied above, you might see a new file appear in your directory - this is a state file.

For any future changes, it will refer back to this state file, and only make any changes which are **different** to what's in this state file

Standard - stores the state file locally, but in real world, will probably be a shared file

---

## Destroy

We can get rid of what we created using one of two methods

`terraform destroy` - destroys everything in your state file

Delete the content of your main.tf file and run `terraform apply` again

---

## Overview - recap

- What is infrastructure as code?
- What are the problems that it solves?
- What is terraform?
- Dive into some terraform

---

## Learning Objectives - recap

- See some HCL (HashiCorp Configuration Language)
- Writing some HCL
- Use Terraform in AWS

---

### Emoji Check:

On a high level, do you think you understand the main concepts of this session? Say so if not!

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:
The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content
