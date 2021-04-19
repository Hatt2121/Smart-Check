import imbox
import smtplib, ssl
import email
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
                download_path = "{}/{}".format(download_folder,att_fn)
                open(download_path,"wb").write(attachment.get('content').read())
            except:
                print(traceback.print_exc())

        mail.mark_seen(uid)

    mail.logout()


def return_attachment(email, item_dict):
    file = open("return_attachment.txt","w")
    for key, value in d.item_dict:
        file.write(str(key) + "\n")

    msg = email.mime.MIMEMultipart()
    msg['From'] = "smartcheck021@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Smart_list"

    attachment = email.mime.text.MimeText(file)
    attachment.add_heaader('Content-Disposition','attachment',filename=file.name)
    msg.attach(attachment)

    try:
        context = ssl.create_deafault_context()
        smtp = smtplib.SMTP_SSL("smtp.gmail.com",465,context = context)
        smtp.login("smartlist021@gmail.com","MatterH27h")
        smtp.sendmail("smartlist021@gmail.com",email,msg.as_string())

    except:
        print("Some sort of network failure happened trying to send the eamil.")
    finally:
        smtp.close()

download_attachment()
