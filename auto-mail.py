import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Reading the password from a file
with open('senha.txt', 'r') as file:
    senha = file.readlines()
file.close()

# Extracting the email password
senha_email = senha[0]
email = 'x@gmail.com'

# Reading the list of recipient emails from a file
with open('lista_emails.txt', 'r') as file:
    emails = file.read().splitlines()

# Creating the email message container
msg = MIMEMultipart()

# Composing the body text of the email
texto_email = '''Olá!\n
Coloque seu texto!
Atenciosamente,\n
X.\n
Telefone: X'''
msg.attach(MIMEText(texto_email))

# Adding an attachment (CV.pdf)
with open('CV.pdf', 'rb') as file:
    cv = file.read()

anexo = MIMEApplication(cv, Name='CV.pdf')
anexo['Content-Disposition'] = f'attachment; filename="CV-ReemFaisal.pdf"'
msg.attach(anexo)

# Adding subject and sender
msg['Subject'] = 'Interesse em Oportunidades de Design de Interiores'
msg['From'] = email

# Connecting to SMTP server and sending emails
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, senha_email)
    
    # Iterating over the list of recipient emails and sending the email
    for destinatario in emails:
        del msg['To']  # Clearing previous recipient
        msg['To'] = destinatario  # Setting new recipient
        smtp.sendmail(email, destinatario, msg.as_string())
        # Uncomment the next line to print the status of each email sent
        # print(f"E-mail enviado para {destinatario}")
