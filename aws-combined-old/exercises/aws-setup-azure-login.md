# AWS Setup using `aws-azure-login`

## AWS Account Access

1. Browse to the AWS (web) console login page
    1. The instructors will give you the URL, please bookmark it
1. This should automatically log you in with role `student-access-role`
    1. if you have more than one role (e.g. instructors only), select the one you need.

---

## AWS CLI Setup

### Installation

**Windows**:

1. Download the [latest version](https://awscli.amazonaws.com/AWSCLIV2.msi)
1. Open the download and follow the installation steps
1. Verify your installation with the following command:
    1. `aws --version`

```sh
C:\> aws --version
aws-cli/2.1.24 Python/3.7.4 Windows/10 botocore/2.0.0
```

Note: you may see a more recent version number.

**MacOS**:

1. Download the [latest version](https://awscli.amazonaws.com/AWSCLIV2.pkg)
1. Open the download and follow the installation steps
1. Verify your installation with the following commands:

```sh
$ which aws
/usr/local/bin/aws

$ aws --version
aws-cli/2.1.24 Python/3.7.4 Darwin/18.7.0 botocore/2.0.0
```

Note: you may see a more recent version number.

**Linux**:

Follow the guide which best matches your setup [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html).

### Configuration

#### Node & NPM

We need at least Node v20+ to run some of our AWS tools.

> Before proceeding, please see the same section `Node & NPM` in [laptop-setup-sot.md](../../laptop-setup-sot/laptop-setup-sot.md).

#### Task - Install aws-azure-login

We will use a tool called `aws-azure-login` to handle logging into AWS via the CLI, which needs to be installed with `npm`.

To install `aws-azure-login` follow the [npm instructions](https://github.com/aws-azure-login/aws-azure-login?tab=readme-ov-file#installation) on the project's github page.

The instructor will now give you three sensitive bits of data. Do not put these into Git, or share them publicly:

- azure_tenant_id e.g. `abc-de-fgh-ij`
- azure_app_id_uri e.g. `klm-nop-qrst`
- aws_account_number e.g. `9876543210`

You will also need:

- full_accenture_email_address E.g. `alice.jones@accenture.com`
- iam_role_arn, which is long and looks something like this: `arn:aws:iam::{aws_account_number}:role/student-access-role`

#### Task - Configure aws-azure-login CLI profile

> The instructor will tell you what your profile name should be

Run `aws-azure-login --configure --profile <profile-name>`, substituting in the values:

```sh
Azure Tenant ID: {azure_tenant_id}
Azure App ID URI: {azure_app_id_uri}
Default Username: {full_accenture_email_address}
Stay logged in: true
Default Role ARN: {iam_role_arn}
Default Session Duration Hours: 1
```

#### Task - set default region

We need to always use the same region in AWS, so we don't unexpectedly create resources in Japan instead of `eu-west-1`!

Run this now:

```bash
aws configure set region eu-west-1 --profile <profile-name>
```

#### Task - log in to AWS

Run the following command to log in to AWS:

```sh
aws-azure-login --profile <profile-name> --mode gui
```

You will be prompted to enter your Accenture account password, you can copy/paste this into your terminal.

#### Task - Saving our profile name

We need to create an environment variable to save our AWS profile. So that we don't need to remember to set this variable every time we need it, we'll add it to our `~/.zshrc` or `~/.bashrc` file:

```sh
echo "export AWS_PROFILE=<profile-name>" >> ~/.bashrc
```

Don't forget to replace `<profile-name>` with the actual profile name!

#### Task - Test the login

Either (a) Source your profile or (b) close your current terminal and make a new one.

> Then, run `aws-azure-login --profile <profile-name>` and check it works.

#### Task - Confirm you can log in!

1. On your terminal, check which user you're using to call the AWS operations by running this:
    1. `aws sts get-caller-identity --profile <profile-name>`
1. Get a list of available S3 buckets by running this:
    1. `aws s3 ls --profile <profile-name>`
1. On the Management Console in your browser:
    1. Search for S3 in the services search box at the top of the page
    1. Select S3 from the list of services
    1. Look at the list of available buckets - does this match what you saw in the terminal?

We'll hear more info on what S3 and buckets are soon!
