from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("You must provide a valid email")

        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username=models.CharField(max_length=255)
    name=models.CharField(max_length=255,null=True,blank=True)
    password=models.CharField(max_length=2555)
    created_date= models.DateField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args,**kwargs):

        if not self.pk:
            self.set_password(self.password)

        self.username=f"{self.username} 1234"
        self.UpdatedDate=timezone.now()+timezone.timedelta(hours=1)

        super(User, self).save(*args,**kwargs)

    def __str__(self):
        return self.email

