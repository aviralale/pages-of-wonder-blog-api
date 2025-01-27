from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

now = timezone.now

class UserManager(BaseUserManager):
    def create_user(
            self,
            email,
            username,
            password=None,
            **extra_fields,
    ):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(
            self,
            email,
            username,
            password=None,
            **extra_fields,
    ):
        user = self.create_user(
            email,
            username,
            password=password,
            **extra_fields,
            )
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_admin", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get("is_staff") is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get("is_admin") is not True:
            raise ValueError('Superuser must have is_admin=True.')
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=255,
        unique=True
    )
    first_name = models.CharField(
        max_length=255,
        default=" "
    )
    last_name = models.CharField(
        max_length=255,
        default=" "
    )
    display_name = models.CharField(
        max_length=255,
        default=f"{first_name, last_name}"
    )
    is_active = models.BooleanField(
        default=False
    )
    is_admin= models.BooleanField(
        default=False
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_superuser = models.BooleanField(
        default=False
    )
    date_joined = models.DateTimeField(
        default= now,
        )
    objects = UserManager
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.username