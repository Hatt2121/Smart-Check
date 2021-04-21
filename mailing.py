'''
    The user needs to install imbox onto the raspberry pi in order to download files from the user's inbox.
    That library is amazing because it simplifies the process A LOT.
'''
import imbox #imbox is something that you need to install.
import smtplib, ssl
import email #also need email library which should come on every python installation... at least.
from email.mime import multipart,text
import os
import traceback

def download_attachment():
    '''
        Will download emails with subject 'smart_list' that are also unread.
        The file itself can be named whatever, but it is gong to be under the file name downloaded_list.txt
    '''
    #filter email in inbox and send the list to us to process
    download_folder = os.path.dirname(os.path.realpath(__file__))
    mail = imbox.Imbox('imap.gmail.com',username='smartcheck021@gmail.com',password='MatterH27h',ssl=True,ssl_context=None,starttls=False)
    messages = mail.messages(unread=True,subject="smart_list", raw='has:attachment')

    #for each email, same download the attachments.
    for (uid, message) in messages:
        for idx, attachment in enumerate(message.attachments):
            try:
                #att_fn = attachment.get('filename') I don't want the folder to be clogged with different files that mean similar things, it's better to call it one file and then override it instead.
                download_path = "{}/{}".format(download_folder,"downloaded_list.txt") #donwload file as "downloaded_list.txt"
                open(download_path,"wb").write(attachment.get('content').read()) #open file just to read.
            except:
                print(traceback.print_exc())

        mail.mark_seen(uid) #mark email as read.

    mail.logout() #logout.


def return_attachment(gmail, item_dict):
    '''
        Creates an attachment and then sends it to the string gmail, from the dictionary item_dict.
        Uses the smtp library.
    '''
    file = open("return_attachment.txt","w")
    for key, value in item_dict.items():
        file.write(str(key) + " " +str(value) + "\n")
    file.close()
    del(file) #for some reason, you have to remove the variable and redo it.

    mjsg = multipart.MIMEMultipart() #create email base.
    mjsg['From'] = "smartcheck021@gmail.com"
    mjsg['To'] = gmail
    mjsg['Subject'] = "Smart_list"

    attn = open("return_attachment.txt","r") #create attachments.
    attachment = text.MIMEText(attn.read())
    attachment.add_header('Content-Disposition','attachment',filename=attn.name)
    mjsg.attach(attachment) #attach attachment... I love documentation.

    try:
        context = ssl.create_default_context() #send email and exit
        smtp = smtplib.SMTP_SSL("smtp.gmail.com",465,context = context)
        smtp.login("smartcheck021@gmail.com","MatterH27h")
        smtp.sendmail("smartcheck021@gmail.com",gmail,mjsg.as_string())
        smtp.close()
    except:
        print("Some sort of network failure happened trying to send the eamil.") #If you get this it means you have problems with either the network or the 'gmail' (email) input.
