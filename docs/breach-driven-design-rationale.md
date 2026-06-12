# Breach-Driven Design Rationale

## Why this project exists

This project was created because recent large-company data breaches have shown how damaging harvested user information can be. Once personal data is stolen, it can be reused beyond the original breached organisation for identity abuse, phishing, credential stuffing, account takeover, fraudulent account creation, and fake identity construction.

## Data at risk

The architecture is designed around protecting high-risk user data, including:

- passwords
- contact details
- National Insurance numbers or equivalent government identity numbers
- account details and customer reference numbers
- biometric-derived verification data such as fingerprint or retina templates

## Design response

The solution reduces the value of a compromised database by ensuring that verification-only sensitive fields are transformed before storage. Passwords are stored as strong salted hashes. Other sensitive values are hashed only when they are needed for matching or verification. If the application must recover the original value, the project documentation recommends encryption or tokenisation instead.

## Why this matters to recruiters

This project demonstrates cloud architecture thinking beyond simply deploying infrastructure. It shows threat modelling, data classification, secure application design, AWS network segmentation, encryption, audit logging, and CI/CD automation using Terraform and GitHub Actions.
