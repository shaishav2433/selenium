import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587)
# print(conn.ehlo()) # for checking connection to server
conn.starttls()
conn.login('xxxxxxxx@gmail.com','......')
#conn.sendmail('to','from','Subject:<type subject line> \n\n<Body of the email>') \n - for new lines
conn.sendmail('xxxxx@gmail.com','xxxx@gmail.com','Subject: GPU - 5700XT temp is reaching high\n\nHello,\n\nThe temperature is approaching quite high, automatic restart has been applied\n\nThanks,\nPython.')
conn.quit()