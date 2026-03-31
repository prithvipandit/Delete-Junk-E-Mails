import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from string import Template
import os

def send_custom_email(sender_email, app_password, receiver_email, subject, template_path, template_data={}, attachment_path=None, smtp_server="smtp.gmail.com", smtp_port=465):
    """
    Sends an email using standard SMTP. Supports HTML templates and generic attachments.
    """
    print(f"Preparing to send email to {receiver_email}...")

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Read and render the HTML template
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
        html_content = Template(template_content).safe_substitute(template_data)
        msg.attach(MIMEText(html_content, 'html'))
    except Exception as e:
        print(f"Error reading or rendering template {template_path}: {e}")
        return False

    # Attach file if provided
    if attachment_path:
        if os.path.exists(attachment_path):
            try:
                with open(attachment_path, "rb") as f:
                    part = MIMEApplication(f.read(), Name=os.path.basename(attachment_path))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
                msg.attach(part)
            except Exception as e:
                print(f"Error attaching file {attachment_path}: {e}")
                return False
        else:
            print(f"Attachment file not found at {attachment_path}. Proceeding without attachment.")

    # Send the email
    try:
        # Use SMTP_SSL for standard Gmail port 465
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully to {receiver_email}!")
        return True
    except smtplib.SMTPException as e:
       print(f"SMTP error occurred: {e}")
       return False
    except Exception as e:
        print(f"An unexpected error occurred while sending email: {e}")
        return False
