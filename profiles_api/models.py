from django.db import models
# Create your models here
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ manager for user profile """

    def create_user(self, email, name, password=None):
        """ create a new user profile """
        if not email:
            raise ValueError("user must have email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        # is_superuser produced with permissionsmixin بخاطر همین داخل یوزرپروفایل تعریفش نکردیم
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=300, unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    # این یعنی که یوزر نیم رو میکنیم ایمیلش
    USERNAME_FIELD = 'email'
    # این یعنی میگیم که نام اجباریه
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name from user"""
        return self.name

    def get_short_name(self):
        """retrieve short name from user"""
        return self.name

    def __str__(self):
        return self.email
