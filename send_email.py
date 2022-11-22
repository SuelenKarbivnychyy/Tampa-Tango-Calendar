# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail



# message = Mail(
#     from_email='suelenmatosr@outlook.com',
#     to_emails=['user0@test.com', 'user1@test.com', 'user2@test.com', 'user3@test.com', 'user4@test.com', 'user5@test.com', 'user6@test.com', 'user7@test.com', 'user8@test.com', 'user9@test.com', 'maria@gmail.com'],
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg = SendGridAPIClient("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")
#     # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)



####################################################################################################################
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email_updates(recipients, subject, content):                                                 #recipients is a list of user emails
    """Sending emails to subscribed"""
    """return True if send email successed return False otherwise """

    message = Mail(
    from_email = 'suelenmatosr@outlook.com',
    to_emails = recipients,
    subject = subject,
    html_content = content)

    result = True

    try:
        sg = SendGridAPIClient("PUT YOUR KEY HERE")
        # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
        result = False

    return result



