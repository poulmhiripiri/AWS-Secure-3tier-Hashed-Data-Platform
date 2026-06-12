# High-Level Architecture

## Purpose

This document describes the high-level design for a secure AWS Multi-AZ 3-tier data capture platform. The system captures user information through a web interface, processes sensitive fields in the application tier, hashes selected values, and stores the resulting hash values in Amazon RDS instead of clear text.

## Design goals

- Improve confidentiality of sensitive user data
- Reduce impact if the database is compromised
- Provide high availability across multiple Availability Zones
- Separate public, application, and database layers
- Use Infrastructure as Code for repeatable deployment
- Use CI/CD automation for controlled cloud deployment
- Apply security controls familiar to enterprise and banking environments

## Logical architecture

The solution is split into three tiers:

### 1. Presentation tier

The presentation tier provides controlled public access to the service.

Components:

- Amazon Route 53 for DNS
- Optional Amazon CloudFront for edge delivery
- AWS WAF for web-layer protection
- Internet-facing Application Load Balancer across two public subnets

### 2. Web and application tier

The web and application services run in private subnets. This avoids exposing EC2 instances directly to the internet.

Components:

- Web tier Auto Scaling Group across two private subnets
- Internal Application Load Balancer
- Application tier Auto Scaling Group across two private subnets
- IAM instance profiles for least-privilege AWS access
- SSM Parameter Store / Secrets Manager for sensitive configuration

The application tier performs the security-critical data transformation. Sensitive values are hashed before being inserted into the database.

### 3. Data tier

The data tier stores user records and hashed sensitive fields.

Components:

- Amazon RDS MySQL deployed in private database subnets
- Multi-AZ configuration for automatic failover
- KMS encryption at rest
- Security group allowing database access only from the application tier

## Availability design

The solution is deployed across two Availability Zones. Each AZ has public, private application, and private database subnets. Load balancers and Auto Scaling Groups span both AZs. RDS uses Multi-AZ deployment to maintain a standby instance in a separate AZ.

## High-level data flow

1. A user submits data through the web interface.
2. DNS routes the request to the public ALB.
3. The public ALB forwards the request to the private web tier.
4. The web tier sends application traffic to the internal ALB.
5. The internal ALB forwards requests to application instances.
6. The application tier validates input and hashes sensitive fields.
7. Only hashed values are stored in Amazon RDS.
8. Logs, metrics, and audit events are sent to CloudWatch and CloudTrail.

## High-Level Architecture Diagram

```mermaid
flowchart TD
    U[Users / Clients] --> R53[Route 53]
    R53 --> WAF[AWS WAF]
    WAF --> ALB[Internet-facing ALB]

    subgraph AWS[AWS Cloud]
      subgraph VPC[VPC across two Availability Zones]
        subgraph AZA[Availability Zone A]
          PUBA[Public Subnet A]
          APPA[Private App Subnet A]
          DBA[Private DB Subnet A]
        end
        subgraph AZB[Availability Zone B]
          PUBB[Public Subnet B]
          APPB[Private App Subnet B]
          DBB[Private DB Subnet B]
        end

        ALB --> WEB[Web Tier Auto Scaling Group]
        WEB --> IALB[Internal ALB]
        IALB --> APP[Application Tier Auto Scaling Group]
        APP --> RDS[(RDS MySQL Multi-AZ)]
      end

      APP --> SSM[SSM Parameter Store / Secrets Manager]
      APP --> KMS[AWS KMS]
      APP --> CW[CloudWatch]
      RDS --> CW
      AWS --> CT[CloudTrail]
    end
```


## Breach-aware data protection objective

This design was created in response to the growing impact of large-company data breaches. The architecture assumes that attackers may attempt to harvest passwords, contact details, National Insurance numbers, account identifiers, and biometric-derived verification data. The system therefore minimises database exposure by storing verification-only sensitive values as hashes, isolating secrets outside the database, and combining application-level protection with AWS network segmentation and encryption controls.
