import smtplib
from smtplib import SMTPServerDisconnected, SMTPAuthenticationError

# creates SMTP session
try:
	s = smtplib.SMTP('smtp.gmail.com', 587)
except SMTPServerDisconnected as e:
	print(e)
	exit()


# start TLS for security
s.starttls()

# Authentication
try:
	s.login("test@gmail.com", "password")
except SMTPServerDisconnected as e:
	print(e)
	exit()
except SMTPAuthenticationError as e:
	print(e)
	exit()

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("test@gmail.com", "receiver@gmail.com", message)

# terminating the session
s.quit()
