from django.db import transaction
from rest_framework import permissions, views
import pyotp
from django.db.models import Q

from django_email_celery.response import not_found, register_successfully, exception_response, login_successfully, \
    get_otp
from user import serializers
from user.tasks import send_otp_mail_task
# Create your views here.
from user.models import User


# from user.send_mail_message import Mailer
# from user_api.response import register_successfully, exception_response, login_successfully, not_found, get_otp


class RegisterUserView(views.APIView):
    # API to register new user with his email and password.
    serializer_class = serializers.UserRegisterSerializer
    permission_classes = (permissions.AllowAny,)

    # @utils.swagger_auto_schema(request_body=serializers.UserRegisterSerializer)
    @transaction.atomic()
    def post(self, request):
        """
        :param request:
        :return:
        """
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return register_successfully()
        except Exception as e:
            return exception_response(e)


class LoginUserView(views.APIView):
    # API to login the the user with his username and password
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserLoginSerializer

    # @utils.swagger_auto_schema(request_body=serializers.UserLoginSerializer)
    @transaction.atomic()
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            return login_successfully(serializer)

        except Exception as e:

            return exception_response(e)


class SendOtpToMail(views.APIView):
    # API to invoke when the user forgot the password
    permission_classes = (permissions.AllowAny,)

    @transaction.atomic()
    def post(self, request):
        try:
            mail_id = request.data.get('email')
            user_mail = User.objects.filter(Q(email=mail_id))
            if not user_mail:
                return not_found()
            base32secret = pyotp.random_base32()
            time_otp = pyotp.TOTP(base32secret, interval=1000)
            time_otp = time_otp.now()
            user_verify = User.objects.get(Q(email=mail_id))
            user_verify.otp = time_otp
            user_verify.save()
            if user_verify:
                return send_email(time_otp, mail_id)
        except Exception as e:
            return exception_response(e)


def send_email(time_otp, mail_id):
    send_otp_mail_task.delay(time_otp, mail_id)
    return get_otp(time_otp)
