from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_otp_mail(otp, mail_id):
    context = {
        'otp': otp,
        'mail_id': mail_id,
    }
    email_subject = 'Account verification'
    email_body = render_to_string('otp_email_msg.txt', context)
    email = EmailMessage(email_subject, email_body, settings.EMAIL_HOST_USER, [mail_id, ],
                         )
    return email.send(fail_silently=False)
