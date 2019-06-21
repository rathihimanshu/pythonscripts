import smtplib
from email.mime.text import MIMEText
import getpass

host_name = 'smtp.gmail.com'
port = 465
u_name = 'himanshu.rathi@talktotechie.com'
password = getpass.getpass()
sender = 'sender_name'
receivers = ['himanshu.rathi@talktotechie.com']

text = MIMEText('Test mail')
text['Subject'] = 'Test'
text['From'] = sender
text['To'] = ', '.join(receivers)

s_obj = smtplib.SMTP_SSL(host_name, port)
s_obj.login(u_name, password)
s_obj.sendmail(sender, receivers, text.as_string())
s_obj.quit()
print("Mail sent successfully")

