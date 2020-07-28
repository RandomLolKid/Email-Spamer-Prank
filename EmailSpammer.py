#LOL Prank ur friend with this :)

import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from datetime import datetime
import os
from os import path, getcwd
from random import randint

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
filedir = getcwd() + "\\Files\\Spam"


filename = None
attachment = None

print("Reading Email And Passowrd!")

configfile = open("Config.txt")
login = {"Email": None, "Password": None}
content = {"Body": None, "Subject": None}

configcontent = configfile.readlines()

login["Email"] = configcontent[0][6:]
login["Passowrd"] = configcontent[1][9:]

useInt = False

if configcontent[3][13] == 1:
	useInt = True
else:
	useInt = False

toe = input("Target Email: ")
content["Subject"] = input("Subject Of The Email: ")
content["Body"] = input("Body Of The Email: ")
times = int(input("How Many Time Do You Want To Send It: "))


frome = login["Email"]

#This value is to ensure that the user wont get the same email
randomint = str(randint(0, 1000000000000)) + str(randint(0, 1000000000000))

for i in range(0, times + 1):
	
	print("Packing mail #" + str(i))
	print("Press Control(ctrl) + c to quit")
	msg = MIMEMultipart() 

	msg['From'] = frome
 
	msg['To'] = toe

	if useInt:
		msg['Subject'] = randomint + content["Subject"]
	else:
		msg['Subject'] = content["Subject"]

	body = content["Body"]

	msg.attach(MIMEText(body, 'plain')) 

	smtp = smtplib.SMTP('smtp.gmail.com', 587) 

	smtp.starttls() 

	smtp.login(frome, login["Passowrd"]) 

	text = msg.as_string() 

	print("Sending Mail")

	smtp.sendmail(frome, toe, text) 
	
	print("Sent Spam #" + str(i) + "---" + str(times - i) + " Times To Go")
	smtp.quit() 
