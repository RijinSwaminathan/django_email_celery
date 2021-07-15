from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings


def send_otp_mail(time_otp, mail_id):
    context = {
        'time_otp': time_otp,
        'mail_id': mail_id,
    }
    email_subject = 'Account verification',
    email_text_body = render_to_string('otp_email_msg.txt', context)
    email_html_body = render_to_string('user_verification.html', context)
    email = EmailMultiAlternatives(email_subject, email_text_body, settings.EMAIL_HOST_USER,
                                   [mail_id, ], )
    email.attach_alternative(email_html_body, "text/html")
    return email.send(fail_silently=False)
