# Recruiter Summary

## Project Title

AWS Secure 3-Tier Hashed Data Capture Platform

## One-Line Summary

Designed and automated a secure AWS 3-tier application that captures user data and stores sensitive fields as salted hash values in RDS, using Terraform and GitHub Actions.

## CV / LinkedIn Bullet Points

- Designed a secure AWS 3-tier architecture using public, private application, and private database subnets across multiple Availability Zones.
- Implemented data confidentiality controls by hashing sensitive user fields before storage, reducing impact in a database compromise scenario.
- Automated cloud infrastructure deployment using Terraform and GitHub Actions CI/CD workflows.
- Applied enterprise security principles including least privilege IAM, KMS encryption, secrets management, CloudTrail auditing, and network segmentation.
- Demonstrated transition from hands-on banking infrastructure and network management into AWS cloud architecture and DevSecOps delivery.

## Skills Demonstrated

AWS VPC, Subnets, Routing, Security Groups, ALB, RDS MySQL, KMS, IAM, SSM / Secrets Manager, CloudWatch, CloudTrail, Terraform, GitHub Actions, Python, Flask, secure hashing, DevSecOps, infrastructure as code.

## Interview Explanation

I built this project to show how my on-prem infrastructure and banking security experience maps into cloud architecture. The design follows a traditional 3-tier model but implements it in AWS using infrastructure as code. A key security feature is that sensitive data is hashed at the application layer before being inserted into the database. Therefore, if the database is compromised, the attacker only obtains salted hash values rather than clear text information.
