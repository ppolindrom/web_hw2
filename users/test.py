
import smtplib
from email.mime.text import MIMEText

def send_mail(to, theme, message):

    file_content = message

    msg = MIMEText(file_content)
    msg['Subject'] = theme
    msg['From'] = 'polinaskypro@yandex.ru'
    msg['To'] = to

    smtp_server = 'smtp.yandex.ru'
    smtp_port = 465
    smtp_username = 'polinaskypro@yandex.ru'
    smtp_password = 'zqwlgljcjdgrdggd'


    s = smtplib.SMTP_SSL(smtp_server, smtp_port)
    s.login(smtp_username, smtp_password)
    s.sendmail('polinaskypro@yandex.ru', [to], msg.as_string())

    s.quit()


