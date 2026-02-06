import smtplib
from email.message import EmailMessage

EMAIL_ADRESS = ""
EMAIL_PASSWORD = ""
DESTINATAIRE = ""

msg = EmailMessage()
msg['Subject'] = "Test"
msg['From'] = EMAIL_ADRESS
msg['To'] = DESTINATAIRE
msg.set_content("Hello world")

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        
    print("email send")
except Exception as e:
    print(f"error : {e}")