import requests 
import pandas as pd
import smtplib
from email.message import EmailMessage

gmail_user = 'dhanush@gmail.com'
gmail_password = 'testpass'

sent_from = gmail_user
to = ['person_a@gmail.com', 'person_b@gmail.com']
subject = 'Server Health Check'
body = 'Endpoint is Down'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)




df = pd.read_csv("endpoints.csv")
for index, endpoints in df.iterrows():
  

  try:
    response=requests.get(endpoints["Name"])
    
  except:
    print("endpoint {} is down".format(endpoints["Name"]))
    

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Email not sent",ex)
