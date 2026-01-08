# Infrastructure as code - Terraform

## Prerequisite

1. install terraform CLI https://www.terraform.io/downloads

1. GCP access configured on your terminal (https://cloud.google.com/sdk/gcloud/reference/auth/login)

1. verify your terraform installation `terraform version`

## Exercise 1 - create a basic template

1. create a new directory in your workspace `devops_terraform`

1. create a new file within the `devops_terraform` directory called `exercise1.tf`

1. add `terraform` configuration block

   ```text
    terraform {
      required_providers {
        google = {
          source  = "hashicorp/google"
          version = "3.5.0"
        }
      }
    }
    ```

1. Add the `provider` block below. Replace `REPLACE_ME` with your GCP project ID

    ```text
    provider "google" {
    project     = "REPLACE_ME"
    region      = "europe-west2"
    }
    ```

1. Add the `resource` block for a [google storage bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket)

    ```text
    resource "google_storage_bucket" "my_exercise_bucket" {
      name     = "REPLACE_ME"
      location = "EU"
    }
    ```

1. Let's validate this template and ensure that we have the correct formatting. Run `terraform validate`

1. In order to have the functionality to create the bucket we need to initiate terraform. Run `terraform init`

1. Run `terraform plan` this will create an execution plan. See below as the expected output

    ```text
    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
      + create
    
    Terraform will perform the following actions:
    
      # google_storage_bucket.my_exercise_bucket will be created
      + resource "google_storage_bucket" "my_exercise_bucket" {
          + bucket_policy_only = (known after apply)
          + force_destroy      = false
          + id                 = (known after apply)
          + location           = "EU"
          + name               = "yourname_exercise_bucket"
          + project            = (known after apply)
          + self_link          = (known after apply)
          + storage_class      = "STANDARD"
          + url                = (known after apply)
        }
    
    Plan: 1 to add, 0 to change, 0 to destroy.
    ```

1. To apply these changes run `terraform apply`. This will rerun the execution plan and prompt you with the following

    ```text
    Do you want to perform these actions?
      Terraform will perform the actions described above.
      Only 'yes' will be accepted to approve.
    
      Enter a value: 
    ```

1. Enter `yes` to apply the changes.

1. Once complete go to the Google Cloud Platform Console and validate that your bucket has been created

## Exercise 2 - update the template

We are going to build on this template and add a file to the bucket using terraform. This can be useful in some cases,
for instance uploading code to a bucket for deployment to a cloud function.

1. Create a new file called `hello.py` and save this in the `devops_terraform` directory

1. Add boilerplate code to this file for returning hello world. You can copy this from [here](https://cloud.google.com/functions/docs/create-deploy-python)

1. Zip this file and name the zip hello.zip - if you are on linux run: `zip hello.zip ./hello.py`

1. In the `exercise1.tf` file add a `resource` block for [google_storage_bucket_object](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_object)

    ```text
        resource "google_storage_bucket_object" "code_object" {
          name   = "index.zip"
          bucket = "${google_storage_bucket.my_exercise_bucket.name}"
          source = "./hello.zip"
        }
    ```

1. Create an execution plan by running `terraform plan`

1. If all looks ok, run `terraform apply`

## Exercise 3 - enable remote state

To enable team collaboration we want to add a `backend` block which will allow us to create a remote state file.

We have to manually create our bucket this cannot be managed by Terraform.

1. Go to the GCP console -> cloud storage and create a bucket with the name `yourname_tf_bucket` with the basic settings.

1. in the `exercise1.tf` file update the `terraform` block and add the `backend`.

    ```text
    terraform {
      required_providers {
        google = {
          source  = "hashicorp/google"
          version = "3.5.0"
        }
      }
      backend "gcs" {
          bucket = "yourname_tf_bucket"
      }
    }
    ```

1. We now need to initialise the backend, so run `terraform init`. You will get a prompt to copy existing state, respond with `yes`

1. You will still see that the statefile `terraform.tfstate` still exist in your directory. Delete this and the backup version.

1. Run `terraform plan`. You should see that there are no changes.
