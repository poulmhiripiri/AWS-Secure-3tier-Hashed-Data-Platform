variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "eu-west-2"
}

variable "project_name" {
  description = "Project name used for resource naming"
  type        = string
  default     = "secure-3tier-hash"
}

variable "vpc_cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.20.0.0/16"
}

variable "db_username" {
  description = "RDS administrator username"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "RDS administrator password"
  type        = string
  sensitive   = true
}

variable "app_pepper" {
  description = "Application pepper used together with per-value salts for hashing"
  type        = string
  sensitive   = true
}
