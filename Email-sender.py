import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, sender_password):
    # Set up the MIME message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Establish connection to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(sender_email, sender_password)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")
    
    finally:
        server.quit()

# Example usage
sender_email = 'dhirajsalunke7350@gmail.com'
receiver_email = 'dhirajsalunkedp@gmail.com'
subject = 'Test Email'
message = 'Hello, this is a test email.'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_password = 'cyba jydk cujw swpw'


send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, sender_password)
