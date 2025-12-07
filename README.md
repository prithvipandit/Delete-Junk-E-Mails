# Gmail Junk Email Cleaner (Python Script)

This Python script helps you automatically **delete all junk/promotional emails** from your Gmail account using IMAP. It is useful for keeping your inbox clean and clutter-free.

---

## Features
- Connects securely to Gmail using **App Password**
- Identifies **junk/promotional emails**
- Deletes them in bulk
- Lightweight and easy to run

---

## Prerequisites
- Python 3.8+
- A Gmail account
- App Password enabled for your Google account

---

## Step 1: Setup Repository & Virtual Environment

Clone this repository and set up the Python virtual environment:

```bash
python -m venv virtual_environment
.\virtual_environment\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Step 2: Generate APP_PASSWORD 

Create App Password and add to script

Generate an App Password (do not use your normal account password).
For Gmail, open: https://myaccount.google.com/apppasswords

Select Mail and the device (or choose Other (Custom name)), then generate the password.

Open script.py and paste the generated App Password into the variables (example):
```python
EMAIL = "myaccount@gmail.com"       
APP_PASSWORD = "<paste_generated_app_password>"    
```

Use imap.mail.yahoo.com for Yahoo account
```python
IMAP_SERVER = "imap.mail.yahoo.com"  # Yahoo 
```

## Step 3: Run the Script
```bash
python script.py
```