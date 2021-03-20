import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .managers import UserManager
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth import get_user_model
# User = get_user_model()

def length_validator(value):
    if not str(value).__len__() == 10:
        raise ValidationError(
            _('%(value)s must be of 10 digits'),
            params={'value': value},
        )


def check_validator(value):
    if not value:
        raise ValidationError(
            _('%(value)s must not be empty'),
            params={'value': value},
        )


def pincode_validator(value):
    if 6 < str(value).__len__() > 6:
        raise ValidationError(
            _('%(value)s must be of length 6'),
            params={'value': value},
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    full_name = models.TextField(validators=[check_validator])
    phone = models.IntegerField(validators=[length_validator])  # 10
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    state = models.TextField(max_length=256, blank=True, null=True)
    country = models.TextField(max_length=256, blank=True, null=True)
    pin_code = models.IntegerField(validators=[pincode_validator])  # 6

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to="uploads/", null=True, storage=OverwriteStorage())
    categories = models.TextField(blank=True, null=True)
