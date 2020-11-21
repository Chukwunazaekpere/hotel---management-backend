from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **bool_fields):
        if not email:
            raise ValueError("An email address must be entered.")
        if not password:
            raise ValueError("Password field cannot be blank.")

        new_user = self.model(
            email = self.normalize_email(email),
            **bool_fields 
            ) 

        new_user.set_password(password)
        new_user.save(using=self.db)
        return new_user

    def create_staff(self, email, password, *args, **bool_fields):
        bool_fields.setdefault('admin', False)
        bool_fields.setdefault('staff', True)

        new_staff = self.create_user(
            email=email,
            password=password,
            **bool_fields
        )
        return new_staff

    def create_superuser(self, email, password, **bool_fields):
        bool_fields.setdefault('admin', True)
        bool_fields.setdefault('staff', True)

        new_superuser = self.create_user(
            email=email,
            password=password,
            **bool_fields
        )
        return new_superuser


class Users(AbstractBaseUser):
    firstname        = models.CharField(max_length=30)
    lastname         = models.CharField(max_length=30)
    username         = models.CharField(max_length=50, blank=True)
    email            = models.EmailField(unique=True)
    password         = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    date_registered  = models.DateTimeField(auto_now_add=True)
    last_login       = models.DateTimeField(auto_now=True)

    staff            = models.BooleanField(default=False)
    active           = models.BooleanField(default=True)
    admin            = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']
    objects         = UserManager()

    class Meta:
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = '@'.join([self.email, self.firstname])
        super().save(*args, **kwargs)
    
    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    
    def has_perm(self, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    



