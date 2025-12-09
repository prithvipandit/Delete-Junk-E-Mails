import imaplib
from utility.construct_search_query import build_search_query


def move_junk_emails_to_trash(email, app_password, imap_server, subjects, junk_senders):
    print("Connecting to mail server...")
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email, app_password)

    try:        
        mail.select('"[Gmail]/All Mail"')
        gmail_query = build_search_query(subjects=subjects, junk_senders=junk_senders)
        
        status, data = mail.uid("SEARCH",None,f'X-GM-RAW "{gmail_query}"')
        
        if status != "OK":
            print("Search failed")
            return

        msg_uids = data[0].split()
        print(f"Found {len(msg_uids)} junk emails")

        if not msg_uids:
            return

        uid_string = b",".join(msg_uids)

        mail.uid("STORE", uid_string, "+X-GM-LABELS", "\Trash")
        mail.expunge()

        print("All junk emails moved to Trash")
        mail.logout()

    except Exception as exception:
        print(f"Exeception Occured while running the script  : {exception}")