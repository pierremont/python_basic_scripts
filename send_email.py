#! /bin/python

import os
import sys
import smtplib
import string
import socket
import getpass


SMSBody="alerta docker"
SUBJECT = "Alerta docker"
TO = "name.surname@gmail.com"
HOSTUSER = getpass.getuser()
HOSTNAME = socket.gethostname()
FROM = HOSTUSER + "@" + HOSTNAME
text = " \r\n" + SMSBody
HOST = "localhost"
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ), "\r\n")
try:
        server = smtplib.SMTP(HOST)
        server.sendmail(FROM, [TO], BODY)
        server.quit()
except SMTPException:
        print "Error: unable to send email"