output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "public_alb_dns_name" {
  description = "Public ALB DNS name"
  value       = aws_lb.public.dns_name
}

output "internal_alb_dns_name" {
  description = "Internal ALB DNS name"
  value       = aws_lb.internal.dns_name
}

output "rds_endpoint" {
  description = "RDS endpoint"
  value       = aws_db_instance.mysql.address
  sensitive   = true
}

output "app_pepper_parameter" {
  description = "SSM parameter name for application pepper"
  value       = aws_ssm_parameter.app_pepper.name
}
