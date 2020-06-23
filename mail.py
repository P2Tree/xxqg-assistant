import sys
import smtplib
from email.mime.text import MIMEText

def send(to_list, cc_list, content, subject):
    sender =
    mail_user =
    mail_pass =
    mail_host = 'smtp.163.com'
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ";".join(to_list)
    msg['Cc'] = ";".join(cc_list)
    try:
        send_smtp = smtplib.SMTP()
        send_smtp.connect(mail_host, 25)
        send_smtp.login(mail_user, mail_pass)
        send_smtp.sendmail(sender, to_list + cc_list, msg.as_string())
        send_smtp.quit()
        print("success")
    except smtplib.SMTPException as e:
        print("error", e)

def send_mail():
    to_list = []
    send(to_list, [], "test_content", "test_sub")

if __name__ == '__main__':
    send_mail()
