from user import views
from django.conf.urls import url

urlpatterns = [
    url(r'register-user/', views.RegisterUserView.as_view(), name='register-user'),
    url(r'login/', views.LoginUserView.as_view(), name='user-login'),
    url(r'send_otp_to_mail/', views.SendOtpToMail.as_view(), name='forgot-password'),
]
