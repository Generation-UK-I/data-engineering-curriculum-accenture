# Equivalent of set -e command on bash. Exits the script when an error occurs
$ErrorActionPreference = "Stop"
$PSNativeCommandUseErrorActionPreference = $true

#### CONFIGURATION SECTION ####
$aws_profile=$args[0] # e.g. sot-academy, for the aws credentials
$team_name=$args[1]# e.g. 'la-vida-mocha' USE YOUR TEAM NAME FOR THIS SESSION - WITH DASHES
$deployment_bucket="$team_name-shopper-deployment-bucket"
#### CONFIGURATION SECTION ####

# Create deployment bucket stack
Write-Output ""
Write-Output "Doing deployment bucket..."
Write-Output ""
aws cloudformation deploy `
    --stack-name $deployment_bucket `
    --template-file deployment-bucket-stack.yml `
    --region eu-west-1 `
    --capabilities CAPABILITY_IAM `
    --profile $aws_profile `
    --parameter-overrides `
      TeamName=$team_name;

# If SKIP_PIP_INSTALL variable is not set or is empty then do a pip install
if (-not $SKIP_PIP_INSTALL) {
    Write-Output ""
    Write-Output "Doing pip install..."
    # Install dependencies from requirements-lambda.txt into src directory with python 3.12
    # On windows may need to use `py` not `python3`
    python3 -m pip install `
        --platform manylinux2014_x86_64 `
        --target=./src `
        --implementation cp `
        --python-version 3.12 `
        --only-binary=:all: `
        --upgrade -r requirements-lambda.txt;
}
else {
    Write-Output ""
    Write-Output "Skipping pip install"
}

# Create an updated ETL packaged template "etl-stack-packaged.yml" from the default "etl-stack.yml"
# ...and upload local resources to S3 (e.g zips files of your lambdas)
# A unique S3 filename is automatically generated each time
Write-Output ""
Write-Output "Doing packaging..."
Write-Output ""
aws cloudformation package `
    --template-file etl-stack.yml `
    --s3-bucket $deployment_bucket `
    --output-template-file etl-stack-packaged.yml `
    --profile $aws_profile;
    
# Deploy the main ETL stack using the packaged template "etl-stack-packaged.yml"
Write-Output ""
Write-Output "Doing etl stack deployment..."
Write-Output ""
aws cloudformation deploy `
    --stack-name "$team_name-shopper-etl-pipeline" `
    --template-file etl-stack-packaged.yml `
    --region eu-west-1 `
    --capabilities CAPABILITY_IAM `
    --capabilities CAPABILITY_NAMED_IAM `
    --profile $aws_profile `
    --parameter-overrides `
      TeamName=$team_name;
      
Write-Output ""
Write-Output "...all done!"
Write-Output ""
