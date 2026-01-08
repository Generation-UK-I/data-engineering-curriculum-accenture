###
### PowerShell Script to deploy S3 bucket in cloudformation stack
###

# PowerShell equivalent of the bash set -eu command. Exits script when error occurs
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$PSNativeCommandUseErrorActionPreference = $true

#### CONFIGURATION SECTION ####
$aws_profile=$args[0] # e.g. sot-academy, for the aws credentials
$your_name=$args[1] # e.g. rory-gilmore (WITH DASHES), for the stack name
#### CONFIGURATION SECTION ####

Write-Output ""
Write-Output "Doing etl stack deployment..."
Write-Output ""
aws cloudformation deploy `
    --stack-name $your_name-shopper-etl-pipeline `
    --template-file etl-stack.yml `
    --region eu-west-1 `
    --capabilities CAPABILITY_IAM `
    --profile $aws_profile `
    --parameter-overrides `
      YourName=$your_name;
      
Write-Output ""
Write-Output "...all done!"
Write-Output ""
