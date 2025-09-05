Daily Weather Email Automation

This repository contains a Python script that sends a daily weather email to a specified recipient. The script is designed to run automatically using GitHub Actions, making it fully cloud-based and requiring no local machine uptime.

Features

Sends a daily email with weather information.

Configurable recipient and sender email.

Supports dummy/test mode for safe testing.

Fully automated via GitHub Actions.

Requirements

Python 3.11+

Packages listed in requirements.txt:

requests
pandas


SMTP email credentials (Gmail, Outlook, etc.)

Setup

Clone the repository

git clone https://github.com/your-username/your-repo.git
cd your-repo


Install dependencies

pip install -r requirements.txt


Configure secrets in GitHub

Go to your repo → Settings → Secrets and variables → Actions → New repository secret

Add:

EMAIL_USER → your email address

EMAIL_PASS → your email password or app password

Configure the script

Update your_script.py:

# Set recipient email
to_email = "real_recipient@example.com"

# Optional: enable dummy/test mode
DUMMY_MODE = True  # True = send only to your test email


In dummy mode, emails are sent only to your address for testing.

GitHub Actions Workflow

Workflow file: .github/workflows/daily_weather.yml

Runs daily at 8 AM UTC automatically.

Can also be triggered manually from the Actions tab.

Example workflow step for sending emails:

- name: Run script
  run: python your_script.py
  env:
    EMAIL_USER: ${{ secrets.EMAIL_USER }}
    EMAIL_PASS: ${{ secrets.EMAIL_PASS }}

Testing

Create a test branch:

git checkout -b test-run
git push origin test-run


Enable DUMMY_MODE = True in the script.

Trigger the workflow manually from the Actions tab.

Check logs and your test inbox to confirm the email is sent.

Usage

To run locally:

python your_script.py


To run automatically:
GitHub Actions handles scheduling; no local action required.

Notes

Never hardcode email credentials — always use GitHub secrets.

Check spam/junk folder if emails are not received.

Switch DUMMY_MODE = False when ready for production.
