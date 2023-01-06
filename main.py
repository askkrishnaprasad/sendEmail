#import smtplib
import datetime as dt

# my_email = "krishnaprasad@myyahoo.com"
# password = "****"

# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="askkrishnaprasad@gmail.com",
#         msg="Subject: Hello \n\n This is the body of email"
#     )

now = dt.datetime.now()
print(now.weekday())
