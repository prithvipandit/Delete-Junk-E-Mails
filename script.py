from utility.move_to_trash import move_junk_emails_to_trash;

EMAIL = "myaccount@gmail.com"       
APP_PASSWORD = "<paste_generated_app_password>"     

IMAP_SERVER = "imap.gmail.com"         # Gmail
# IMAP_SERVER = "imap.mail.yahoo.com"  # Yahoo


subjects = ["sale", "offer", "deal", "unsubscribe"]

junk_senders = [
        "noreply@eduonix.com",
        "info.tcsionhub@tcsion.com",
        "expertspeak@techgig.com",
        "user@techgig.com"
    ]

if __name__ == "__main__":
    move_junk_emails_to_trash(email=EMAIL, 
            app_password=APP_PASSWORD, 
            imap_server=IMAP_SERVER, 
            junk_senders=junk_senders,
            subjects=subjects)