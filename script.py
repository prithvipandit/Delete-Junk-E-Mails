from utility.move_to_trash import move_junk_emails_to_trash;
from utility.send_email import send_custom_email;

EMAIL = "myaccount@gmail.com"       
APP_PASSWORD = "<paste_generated_app_password>"    

IMAP_SERVER = "imap.gmail.com"         # Gmail
# IMAP_SERVER = "imap.mail.yahoo.com"  # Yahoo

SMTP_SERVER = "smtp.gmail.com"         # Gmail SMTP
SMTP_PORT = 465                        # SSL Port

subjects = ["sale", "offer", "deal", "unsubscribe"]

RECEIVER_EMAIL = "prithvizhi23@gmail.com"

junk_senders = [
        "noreply@eduonix.com",
        "info.tcsionhub@tcsion.com",
        "expertspeak@techgig.com",
        "user@techgig.com"
    ]

if __name__ == "__main__":
    # 1. Clean up junk emails
    # print("--- Starting Junk Cleanup ---")
    # move_junk_emails_to_trash(email=EMAIL, app_password=APP_PASSWORD, imap_server=IMAP_SERVER, junk_senders=junk_senders,subjects=subjects)
    
    # 2. Example: Send a custom email
    print("\n--- Starting Email Sender Example ---")
    
    # These variables will replace ${variable_name} in the HTML template
    template_data = {
        "recruiter_name": "Alice Smith",
        "company_name": "Google",
        "role_name": "Senior Software Engineer",
        "years_of_experience": "3+ Years",
        "sender_name": "Piyush Kumar",
        "sender_email": "piyushpandiit@gmail.com",
        "sender_phone": "+91 90272 88186",
        "linkedin_url": "https://linkedin.com/in/piyush-kumaar",
        "github_url": "https://github.com/prithvipandit"
    }
    
    # Uncomment and fill in RECEIVER_EMAIL below to test sending!
    # RECEIVER_EMAIL = "target@example.com"
    email_subject = f"Exploring {template_data['role_name']} Opportunities at {template_data['company_name']} — {template_data['sender_name']}"
    
    send_custom_email(
        sender_email=EMAIL,
        app_password=APP_PASSWORD,
        receiver_email=RECEIVER_EMAIL,
        subject=email_subject,
        template_path="templates/email_template.html",
        template_data=template_data,
        attachment_path="Piyush.pdf",
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT
    )
