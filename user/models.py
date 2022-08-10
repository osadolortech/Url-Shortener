from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email,password,password2,**extra_fields):
        if not email:
            raise ValueError("email filed is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password2)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('name','admin')
        extra_fields.setdefault('password2', None)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("superuser must have is superuser as True")
        return self.create_user(email,password,**extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=125)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
