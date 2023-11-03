
from flask_mail import Message
from portfolioPortal.cv_app import mail


def send_contact_email(name, company, email, subject, users_message):
    token = ""
    msg = Message(subject,
                  sender='noreply@demo.com',
                  recipients=["eliruffin.tech@gmail.com"])
    msg.body = f'''
Name: 
{name}
Company: 
{company}
Message Content:
{users_message}

Supplied Email: 
{email}
'''
    mail.send(msg)


def send_reply_email(name, supplied_email, company):
    subject = "Confirmation: Your Message to Elijah Ruffin"

    msg = Message(subject=subject,
                  sender='noreply@ruffin.bio',
                  recipients=[supplied_email])
    msg.body = f'''
Dear {name},

Thank you for taking the time to fill out the contact form on my portfolio website. I'm thrilled to hear from you and appreciate your interest in my work.

Your inquiry is important to me, and I aim to respond as quickly as possible. In the meantime, feel free to explore other sections of my portfolio to learn more about my experience, projects, and skills.
If you have any immediate questions or would like to discuss a specific opportunity, don't hesitate to reply to this email or contact me through my social media platforms.

Thank you once again for reaching out. I look forward to the possibility of collaborating with you at {company} in the near future.

Best regards,
Elijah Ruffin

    '''
    mail.send(msg)
