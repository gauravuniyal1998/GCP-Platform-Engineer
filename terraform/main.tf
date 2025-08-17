# main.tf
resource "google_storage_bucket" "terraform_bucket" {   
  name          = "${var.project_id}-terraform-bucket"
  location      = var.region
  force_destroy = true
  uniform_bucket_level_access = true
}

