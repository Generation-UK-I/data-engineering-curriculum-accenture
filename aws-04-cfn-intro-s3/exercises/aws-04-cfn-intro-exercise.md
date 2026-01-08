# aws-04-cfn-intro-exercise

## Stack template

We need to start from the mostly empty file [../handouts/etl-stack.yml](../handouts/etl-stack.yml).

- There is already a parameter for your name
- Add a valid S3 bucket using your name
    - Find the `# TODO add ShopperRawDataBucket` comment in the file
    - Add it, following the slides
- Add the bucket policy we need
    - Find the `# TODO Add ShopperRawDataBucketPolicy` comment in the file
    - Add it, following the slides

## Log into AWS

- Open a terminal in the [handouts](../handouts/) folder
    - If using Windows this can be in Powershell
- Log in depending on your AWS login method
- Run
    - Either `aws sso login --profile <your-profile-name>`
    - or `aws-azure-login --profile <you-profile-name>`
    - or use your alias

### Deploy

> The deploy script you need is done for you, so it will reliably work.

It does the following:

- Collect your `aws-profile` and `your-name` from the command line
- Use these to deploy a stack called `your-name-shopper-etl-pipeline`

Run the deploy script like this:

```sh
./deploy.[sh|ps1] <aws-profile> <your-name>
# e.g run one of these:
./deploy.sh sot-academy rory-gilmore # MacOS / WSLv2 / GitBash
./deploy.ps1 sot-academy rory-gilmore # Powershell
```

## Validation

- Open the AWS (web) Console for CloudFormation and check the deployment
    - Check the CloudFormation events on your Stack
    - Check the bucket
