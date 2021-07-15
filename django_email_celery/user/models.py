from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models


# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        :param email:
        :param password:
        :return: Create and return a user with email,username and password
        """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email),
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        :param email:
        :param password:
        :return: Create and return a user with superuser permissions.
        """
        if password is None:
            raise TypeError('Superuser must have a password')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email_address', max_length=255, unique=True)
    otp = models.IntegerField(verbose_name='one_time_password', blank=True, null=True)
    verified_user = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Meta:
    """
    to set table name in database
    """
    db_table = "users"


def __str__(self):
    return self.email
