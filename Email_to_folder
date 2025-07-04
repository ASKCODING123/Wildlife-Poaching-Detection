import imaplib
import email
from email.header import decode_header
import os


username = "d1b2m3s4@gmail.com"
password = "xubr auwd weal wexf"


imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)


imap.select("inbox")


status, messages = imap.search(None, '(UNSEEN)')


folder_name = "Downloaded_Photos"
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
    print(f"Folder created: {folder_name}")


for num in messages[0].split():
    res, msg = imap.fetch(num, "(RFC822)")
    print(f"Processing email {num}")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])

            if msg.is_multipart():
                for part in msg.walk():
                    print(f"Part content type: {part.get_content_type()}")
                    if part.get("Content-Disposition") is None:
                        continue

                    filename = part.get_filename()
                    print(f"Filename: {filename}")
                    if filename and (filename.lower().endswith((".jpg", ".jpeg", ".png"))):
                        filepath = os.path.join(folder_name, filename)
                        print(f"Saving to {filepath}")
                        with open(filepath, "wb") as f:
                            f.write(part.get_payload(decode=True))
                        print(f"Downloaded: {filename}")
            else:
                filename = msg.get_filename()
                print(f"Filename: {filename}")
                if filename and (filename.lower().endswith((".jpg", ".jpeg", ".png"))):
                    filepath = os.path.join(folder_name, filename)
                    print(f"Saving to {filepath}")
                    with open(filepath, "wb") as f:
                        f.write(msg.get_payload(decode=True))
                    print(f"Downloaded: {filename}")


imap.logout()
