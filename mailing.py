import imbox
import os
import traceback

def download_attachment():
    '''
        Will download emails with subject 'smart_list' that are also unread
    '''
    download_folder = os.path.dirname(__file__)
    mail = imbox.Imbox('imap.gmail.com',username='smartcheck021@gmail.com',password='MatterH27h',ssl=True,ssl_context=None,starttls=False)
    messages = mail.messages(unread=True,subject="smart_list", raw='has:attachment')

    for (uid, message) in messages:
        for idx, attachment in enumerate(message.attachments):
            try:
                att_fn = attachment.get('filename')
                download_path = f"{download_folder}"
                open(download_path).write(attachment.get('content').read())
            except:
                print(traceback.print_exc())

        mail.mark_seen(uid)

    mail.logout()

download_attachment()