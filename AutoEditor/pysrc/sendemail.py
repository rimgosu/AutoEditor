import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def send_email(videos):

    now = datetime.now()

    smtp_user = 'newnyup@gmail.com'
    smtp_password = 'pzysqqxextbgmlgh'
    emails = ['practice93@naver.com']
    server = 'smtp.gmail.com'
    port = 587
    
    texts = "Auto edit completed!" + "\n" 
    for video in videos:
        texts += video + "\n"

    for email in emails:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Auto edit completed! ' + str(now)
        msg['From'] = smtp_user
        msg['To'] = email
        text = MIMEText(texts)
        msg.attach(text)

    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.login(smtp_user, smtp_password)
    s.sendmail(smtp_user, email, msg.as_string())
    s.quit()

if __name__ == "__main__":
    send_email("테스트 메일입니다")