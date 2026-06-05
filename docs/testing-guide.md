# Testing Guide

## Local Application Test

```bash
cd app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export APP_PEPPER='local-development-pepper'
python app.py
```

Submit a test user:

```bash
curl -X POST http://localhost:8080/users \
  -H 'Content-Type: application/json' \
  -d '{
    "first_name":"Jane",
    "last_name":"Doe",
    "email":"jane@example.com",
    "password":"SuperSecretPassword!",
    "national_id":"AB123456C",
    "phone_number":"+441234567890"
  }'
```

Expected behaviour:

- API returns non-sensitive user details only.
- Sensitive fields are represented as hash values in the data layer.
- Clear-text password, national ID, and phone number are not returned.

## Terraform Validation

```bash
cd terraform
terraform init
terraform fmt -check
terraform validate
terraform plan
```

## GitHub Actions Validation

Open a pull request into `main`. The workflow should:

1. Check out the code.
2. Configure AWS credentials using OIDC.
3. Run Terraform format check.
4. Run Terraform init.
5. Run Terraform validate.
6. Produce a Terraform plan.

On push to `main`, the workflow can apply the infrastructure if enabled.
