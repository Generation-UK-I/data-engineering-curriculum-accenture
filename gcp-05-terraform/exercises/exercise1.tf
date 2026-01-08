terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  project     = "REPLACE_ME"
  region      = "europe-west2"
}

resource "google_storage_bucket" "my_exercise_bucket" {
  name     = "REPLACE_ME"
  location = "EU"
}

resource "google_storage_bucket_object" "code_object" {
  name   = "index.zip"
  bucket = "${google_storage_bucket.my_exercise_bucket.name}"
  source = "./hello.zip"
}
