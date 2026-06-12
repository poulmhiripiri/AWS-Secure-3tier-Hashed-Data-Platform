# PowerPoint Interview Presentation Outline

## Slide 1 - Project title
Secure AWS Multi-AZ 3-Tier Hashed Data Platform.

## Slide 2 - Problem and business requirement
Protect sensitive user data and reduce exposure if the database is compromised.

## Slide 3 - High-Level Architecture
Users, ALB, private web/app tier, RDS Multi-AZ, KMS, CloudWatch, CloudTrail.

## Slide 4 - AWS Detailed Architecture
Route 53, WAF, public ALB, private compute, RDS, Secrets Manager, SSM, NAT per AZ.

## Slide 5 - Data confidentiality design
Hash sensitive fields before database storage. Use encryption or tokenisation when original values must be recovered.

## Slide 6 - CI/CD and Infrastructure as Code
GitHub Actions validates, plans, and applies Terraform.

## Slide 7 - Operations and resilience
Multi-AZ, Auto Scaling, RDS failover, CloudWatch, CloudTrail, VPC Flow Logs.

## Slide 8 - Recruiter value
Bridges banking infrastructure, enterprise networking, cloud architecture, automation, and security engineering.
