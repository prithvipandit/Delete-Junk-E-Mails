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
    
    from utility.recuriter_details import recruiters

    # 2. Example: Send custom emails to all recruiters
    print("\n--- Starting Bulk Email Sender ---")

    # Common details about the sender format for the template
    sender_info = {
        "years_of_experience": "3.5+ Years",
        "sender_name": "Piyush Kumar",
        "sender_email": "piyushpandiit@gmail.com",
        "sender_phone": "+91 90272 88186",
        "linkedin_url": "https://linkedin.com/in/piyush-kumaar",
        "github_url": "https://github.com/prithvipandit"
    }

    for idx, recruiter in enumerate(recruiters, start=1):
        print(f"\n[{idx}/{len(recruiters)}] Preparing email for {recruiter['recruiter_name']} at {recruiter['company_name']}...")
        
        # Merge common sender variables with this specific recruiter's details
        template_data = {**sender_info, **recruiter}
        
        email_subject = f"Exploring {template_data['role_name']} Opportunities at {template_data['company_name']} — {template_data['sender_name']}"
        
        # Execute the custom email sending logic row by row
        success = send_custom_email(
            sender_email=EMAIL,
            app_password=APP_PASSWORD,
            receiver_email=template_data['recruiter_email'],
            subject=email_subject,
            template_path="templates/email_template.html",
            template_data=template_data,
            attachment_path="Piyush.pdf",
            smtp_server=SMTP_SERVER,
            smtp_port=SMTP_PORT
        )

        if success:
            print(f"-> Mail sent gracefully to {template_data['recruiter_email']}")
        else:
            print(f"-> Failed to send mail to {template_data['recruiter_email']}")
