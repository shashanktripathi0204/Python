import smtplib

to_email ="dummytestmial@outlook.com"

my_email = "dummytest.mail01t@gmail.com"
password = "cghjlaloqcpbrzhq"

connection = smtplib.SMTP("smtp.gmail.com")
# makes the content of the mail encrypted
connection.starttls()
connection.login(user = my_email, password = password)
connection.sendmail(from_addr=my_email, to_addrs = to_email, msg = "Hello ji")
connection.close()