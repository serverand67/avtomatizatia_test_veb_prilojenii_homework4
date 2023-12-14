import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def sendemail():
    fromaddr = "test_mail_to_test@mail.ru"
    toaddr = "test_mail_to_test@mail.ru"
    mypass = "P8qZTdwu1LbWkbmgLvp4"
    reportname = r"C:\Users\NiKa\PycharmProjects\avtomatizatia_test_veb_prilojenii\homework4\log.txt"

    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = "Отчет по тестам"

    with open(reportname, "rb") as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachement; filename="%s"' %basename(reportname)
        msg.attach(part)

    body = "Отчеты по проведенным тестам"
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


if __name__ == '__main__':
    sendemail()
