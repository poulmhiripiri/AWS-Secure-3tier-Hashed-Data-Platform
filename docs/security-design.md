# Security Design

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
