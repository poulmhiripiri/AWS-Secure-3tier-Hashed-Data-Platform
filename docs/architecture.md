# Architecture Design

## Purpose

This project demonstrates how to build a secure AWS 3-tier system that captures user information while protecting sensitive fields from database exposure. The main confidentiality control is application-level one-way hashing before data is persisted.

## Tiers

### Presentation Tier

- Public Application Load Balancer.
- Web entry point reachable from the internet.
- Only forwards approved traffic to the private application tier.
- Security group allows inbound HTTPS/HTTP from the internet and outbound only to the application tier.

### Application Tier

- Runs in private subnets.
- No direct inbound internet access.
- Responsible for validation, hashing, and database writes.
- Retrieves hashing pepper from AWS Secrets Manager or SSM Parameter Store.
- Uses IAM role-based access rather than embedded credentials.

### Data Tier

- Amazon RDS MySQL in private database subnets.
- `publicly_accessible = false`.
- Inbound traffic allowed only from the application tier security group.
- Storage encrypted using AWS KMS.

## Data Flow

1. User submits data through the web endpoint.
2. The request reaches the public Application Load Balancer.
3. The web tier forwards the request to the private application tier.
4. The application validates the data.
5. Sensitive fields are salted and hashed with PBKDF2-HMAC-SHA256.
6. Only hash values are written to RDS.
7. Clear-text sensitive data is never stored in the database.

## Why This Matters

If an attacker compromises the database, they see only hash strings. They do not receive the original values, the application pepper, or the ability to reverse the hashes. This reduces the business impact of a database compromise.
