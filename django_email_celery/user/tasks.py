# from __future__ import absolute_import, unicode_literals
#
# from celery import shared_task
#
#
# @shared_task
# def add(x, y):
#     return x + y
from .email import send_otp_mail
from celery.utils.log import get_task_logger
from celery.decorators import task

logger = get_task_logger(__name__)


@task(name='send_otp_mail')
def send_otp_mail_task(otp, mail_id):
    logger.info('send otp')
    return send_otp_mail(otp, mail_id)
