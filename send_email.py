import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#function to send emails using sendgrid api

def send_email_updates(recipients, subject, content):            #function definition                      #recipients is a list of user emails
    """Sending emails to subscribed"""
    """return True if send email successed return False otherwise """

    message = Mail(
    from_email = 'suelenmatosr@outlook.com',
    to_emails = recipients,
    subject = subject,
    html_content = content)

    result = True

    try:
        sg = SendGridAPIClient(os.environ.get('EMAIL_KEY'))            # instance of class
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:                                              #if there is an error this let you handle the error instead of break the program
        print(e.message)
        result = False

    return result



