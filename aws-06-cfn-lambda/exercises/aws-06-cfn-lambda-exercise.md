# aws-06-cfn-lambda-exercise.md

## Stack template

We need to start from the partially complete file [../handouts/etl-stack.yml](../handouts/etl-stack.yml)

> Values and further steps can be found in the slides for this section

- Add a parameter for Network Stack Name, so we know where to put the lambda
- Add a Lambda with a dynamic name (from Your Name)
- Add a Notification Configuration to the CSV bucket, so that files arriving there wake up the lambda
- Add dependencies to the CSV Bucket
- Add a Source Bucket Permission, so the Lambda is allowed to look in the bucket

## Log into AWS

- Open a terminal in the [handouts](../handouts/) folder
    - If using Windows this can be in Powershell
- Log in depending on your AWS login method
    - If on windows, you can run the below commands in PowerShell
- Run
    - Either `aws sso login --profile <your-profile-name>`
    - or `aws-azure-login --profile <you-profile-name>`
    - or use your alias

## Deployment

- Check your terminal is in the [handouts](../handouts/) folder
    - If using Windows this can be in Powershell

Run the relevant `./deploy.[sh|ps1]` script like this:

```sh
cd handouts
./deploy.[sh|ps1] <aws-profile> <your-name>
# e.g run one of these:
./deploy.sh sot-academy rory-gilmore # MacOS / WSLv2 / GitBash
./deploy.ps1 sot-academy rory-gilmore # Powershell
```

## Validation

- Open the AWS (web) console and check the deployment
    - Check the CloudFormation events on your Stack
    - Check the bucket
    - Check your Log Group for the latest Log Stream
