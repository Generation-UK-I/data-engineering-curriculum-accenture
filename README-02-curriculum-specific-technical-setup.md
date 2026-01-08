# Instructor Course Setup

This guide will help you to setup other configurations/tools specific to this course's curriculum.

> See also the list of related resources in the main [./README.md](./README.md).

## Tutor AWS Access (For Accenture / SoT / Next Gen)

AWS access is through Accenture SSO using your usual credentials for your Accenture / Microsoft account / laptop /etc.

Request one of the Academy Lead Instructors (Mark Matthews and Vicki Cole) to add yourself to the Members of the 2 Active Directory (AD) Groups below and to provide you with the sensitive information that is needed AWS CLI set up;

- [AWS_745580839125_AcademyInstructorAccess](https://aad.portal.azure.com/#view/Microsoft_AAD_IAM/GroupDetailsMenuBlade/~/Members/groupId/ad4d3bd8-3452-419b-bd17-f9bd1b57911d).

- [AWS_745580839125_student-access-role](https://aad.portal.azure.com/#view/Microsoft_AAD_IAM/GroupDetailsMenuBlade/~/Members/groupId/d0ece4b0-d837-495a-a437-f7bce567fa00/menuId/).

- ```sh
  azure_tenant_id=abcd-1234-efgh-56789-thisisnotreal
  azure_app_id_uri=hgfe-9876-dcba-4321-dontcopythis
  azure_default_username=MY.EID@accenture.com
  azure_default_role_arn=arn:aws:iam::123456789:role/NotARealRole
  azure_default_duration_hours=1
  azure_default_remember_me=true
  region=some-where-2
  ```

Follow the AWS setup steps within the [AWS 02 CLI setup](./aws-02-cli-setup/). The information provided in step one will be needed for this, the steps include; `Installing AWS CLI`, `Configuring Env Vars`, and Setup of `aws-azure-login`.

## Student AWS Access (For Accenture / SoT / Next Gen)

AWS access is through Accenture SSO using your usual credentials for your Accenture / Microsoft account / laptop /etc.

Request one of the School of Tech Lead Instructors (Mark Matthews and Vicki Cole) to add your students to the Members of the two Active Directory (AD) Group below and to provide you with the sensitive information they need for AWS CLI set up;

- [AWS_745580839125_student-access-role](https://aad.portal.azure.com/#view/Microsoft_AAD_IAM/GroupDetailsMenuBlade/~/Members/groupId/d0ece4b0-d837-495a-a437-f7bce567fa00/menuId/)

- [School of Tech github org](https://github.com/orgs/IW-Academy) (org has an old name in he link, sorry).

It is also useful to provide them with a link the AWS console to force single sign on for them.

### Core Infrastructure repo

There is a repository that sets up the core infrastructure for the AWS sessions using CDK.

For the School of Tech NJ Academy:

- https://github.com/infinityworks/academy-core-infra
- You have to be in the [IW GitHub org](https://github.com/orgs/infinityworks/teams/staff) to see this, and in one of the [Teaching related teams](https://github.com/orgs/infinityworks/teams?query=teaching).

Then;

- Check out the repo,
- Follow the steps in it's main README.md.

## Make commands for managing AWS resources:

```sh
make delete-lambdas    # Delete all lambdas for AWS an account with 'make delete-lambdas p=aws_sso_profile'
make delete-s3-buckets # Delete all S3 buckets for an AWS account with 'make delete-s3-buckets p=aws_sso_profile'
```

## Containerisation

For those who would prefer to use podman rather than docker, the CLI should be interchangeable and the quickest way to get up and running with the make commands is to alias docker to podman:

`alias docker="podman"`

Troubleshooting tip (Feb 2024): We have observed issues with running podman desktop on M1 Macs. To solve the problem where the podman VM hangs during startup, follow the steps in [this github issue comment](https://github.com/containers/podman/issues/21088#issuecomment-1871502921).
