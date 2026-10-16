terraform {
  cloud {
    organization = "CAD_Backend_23405724"

    workspaces {
      name = "cad_backend"
    }
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.92"
    }
  }

  required_version = ">= 1.2"
}
