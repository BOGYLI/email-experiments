# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Hallo, die ist ein Test.")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Testmail'
msg['From'] = 'mickey@mouse.io'
msg['To'] = 'fakemailreceiver.pension987@passinbox.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
