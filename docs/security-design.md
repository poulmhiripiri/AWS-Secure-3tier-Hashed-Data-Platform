# Security Design


## Threat Scenario: Database Compromise After a Major Breach

The project is designed around a realistic breach scenario: attackers gain access to the application database or export user tables after exploiting stolen credentials, misconfiguration, vulnerable third-party tooling, or insufficient segmentation. The objective is to ensure that the database does not contain reusable clear-text identity data.

The main risks being addressed are:

- credential reuse and password spraying across other platforms
- identity fraud using National Insurance numbers, account details, and contact data
- fake identity creation using harvested identity attributes
- account takeover where personal details are used to pass weak verification checks
- irreversible harm from exposed biometric data, because fingerprints and retina patterns cannot simply be reset like passwords

Security response in this architecture:

1. Sensitive values are processed in the private application tier.
2. Verification-only values are transformed into strong salted hashes before persistence.
3. The application pepper is stored outside the database in AWS Secrets Manager / SSM Parameter Store.
4. RDS is private, encrypted with KMS, and only reachable from the application security group.
5. CloudTrail, CloudWatch, and VPC Flow Logs support investigation and audit evidence.


## Hashing Strategy

The application uses PBKDF2-HMAC-SHA256 with:

- Per-value random salt.
- High iteration count.
- Application pepper stored outside the database.
- Constant-time comparison for verification workflows.

The stored format is:

```text
pbkdf2_sha256$iterations$salt$hash
```

## Hashing vs Encryption

Hashing is one-way and is appropriate when the system only needs to verify a value later. Examples include passwords or high-risk identifiers used only for matching.

Encryption is reversible and is appropriate when the business must retrieve the original value. Examples include address, customer notes, or documents that must be displayed back to authorised users.

This project intentionally hashes sensitive fields to demonstrate confidentiality if the database alone is compromised.

## Threat Model

| Threat | Control |
|---|---|
| Database compromise | Sensitive values stored only as salted hashes |
| Direct database exposure | RDS in private subnets, not publicly accessible |
| Credential leakage in code | Secrets stored in GitHub Secrets, AWS Secrets Manager, or SSM |
| Lateral movement | Tier-based security groups and subnet separation |
| Unauthorised AWS API actions | IAM least privilege and CloudTrail auditing |
| Data at rest exposure | KMS encryption for RDS and log storage |

## Banking/Enterprise Alignment

The design reflects controls commonly expected in regulated environments:

- Defence in depth.
- Network segmentation.
- Audit trail.
- Least privilege access.
- Secure SDLC and infrastructure automation.
- Data confidentiality by design.
