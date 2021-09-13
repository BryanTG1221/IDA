import smtplib

gmail_user = 'asistentepersonal26@gmail.com'
gmail_password = 'Nunc4XD21'

sent_from = gmail_user
to = ['asistentepersonal26@gmail.com', 'moreno12211@outlook.com']
subject = 'Esto es una prueba'
body = 'Hola soy tu asistente personal MARIA!!, este correo es para verificar que la nueva funcion tenga un impacto positivo TQM'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)