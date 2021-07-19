#!/usr/bin/python3
import smtplib

s=smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login("rohit11dhore@gmail.com","***********")

subject1 = 'Important'

message1 = "Your code has been failed, please debug it asap."

s.sendmail("Dugudugude@gmail.com",message1)

s.quit()
