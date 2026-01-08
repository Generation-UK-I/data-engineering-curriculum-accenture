# Terraform Cheatsheet

## Terraform CLI Commands

### Format and Validate

```shell
# Format the terraform code to HCL standards
terraform fmt
# Validate the code for syntax errors
terraform validate
```

### Initialise your working directory

```shell
#Initialise the directory and download providers
terraform init
# Upgrade previously installed plugins to the newest version as defined in configuration
terraform init -upgrade
```

### Plan your infrastructure

```shell
# create execution plan
terraform plan
# create execution plan with variables passed in
terraform plan -var-file=<your_tfvars_file>
# write excution plan to file
terraform plan -out=<filename>
```

### Create your infrastructure

```shell
# create execution plan and execute it - requires approval
terraform apply
# create execution plan and execute it without approval 
terraform apply --auto-approve
# create execution plan and execute it. use definitions from a tfvars file.
terraform apply -var-file=<your_tfvars_file>
```

### Tear down your infrastructure

```shell
# destroys all objects managed by terraform - requires approval
terraform destroy
# destroys all objects managed by terraform - without approval
terraform destroy --auto-approve
# create a destroy execution plan without applying them
terraform plan -destroy
```

### FYIs

```shell
# list all the managed resources tracked by the state file
terraform state list
# imports an existing resource into terraform
terraform import <resouece>.<resource_name> <id> #id is dependent on the resource - check provider documentation for details.
# list all outputs stated in code
terraform output
#get current terraform version
terraform version
```
