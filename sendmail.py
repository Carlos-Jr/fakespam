import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time

with open('dados.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['full_name'], row['mail'])
        name = row['full_name'].split()[0]
        email_header = "Olá " + name+" tudo bem?"
        email_footer = "\n\n\nAtt, \n Carlos Dias"

        msg = MIMEMultipart()
        message = email_header + "Sua chave para acessar o sistema é " + \
            row['token']+email_footer
        password = "coloqueaquiasenha"
        msg['From'] = "seuemail@gmail.com"
        msg['To'] = row['mail']
        msg['Subject'] = "Assunto do email"
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        time.sleep(1)
