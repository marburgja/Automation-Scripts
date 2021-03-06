#! /usr/bin/env python3
# Script Name:      servercheck
# Author:           marburgja
# Last Rev:         20211005
# Purpose:          verify selected machines are network operational
# Reference:        https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python

# Libraries
import os
import time
from time import gmtime, strftime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Variables
ip=input("Enter IP Address:")
sender_address='joshm581@gmail.com'
sender_pass='xxxxxxxxxx' #password
receiver_address='joshm581@gmail.com'
server_status=1

# Main
while True:
    time.sleep(2)
    ping=os.system("ping -c 1 " + ip + "> /dev/null") #to reference ping without having it show up in terminal
    current_time=strftime("%x %X", gmtime())
    message=MIMEMultipart()
    message['From']=sender_address
    message['To']=receiver_address
    message['Subject']='A Server Has Changed Status'

    # print to terminal 'server availability
    if ping == 0:
        print (ip + " is AVAILABLE " + current_time)
    else:
        print(ip + " is UNAVAILABLE " + current_time)

    if ping != server_status:
        if ping == 0:
            mail_contentup=(ip + " is now AVAILABLE " + current_time) #email "body"
            message.attach(MIMEText(mail_contentup, 'plain')) # attaching above variable to email
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string() # convert the message to string and assign to text variable
            session.sendmail(sender_address, receiver_address, text) # yeet that email out
            session.quit()
        else:
            mail_contentdown=(ip + " is now UNAVAILABLE " + current_time) #email "body"
            message.attach(MIMEText(mail_contentdown, 'plain')) # attaching above variable to email
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string() # convert the message to string and assign to text variable
            session.sendmail(sender_address, receiver_address, text) # yeet that email out
            session.quit()
    server_status=ping # change server_status variable to the new status given from ping



# End