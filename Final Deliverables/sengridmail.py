import os
from dotenv import load_dotenv

load_dotenv()
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendmail(usermail,subject,name,content):
    message = Mail(from_email='73151913106@smartinternz.com',to_emails=usermail,subject=subject,html_content='<h4>Hello {}, </h4><br/><strong> {} </strong><br/><p>Best Wishes,</p><p>Team Plasma</p>'.format(name,content))
    try:
        sg = SendGridAPIClient(os.getenv('API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
