from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class UserData(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    #is_admin = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f'{self.first_name or ""} {self.last_name or ""}'

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'





#
# class UserProfile(models.Model):
#     user = models.OneToOneField(UserData, on_delete=models.CASCADE)
#     phone = models.CharField(
#         max_length=20,
#         null=True,
#         blank=True,
#     )
#     about_me = models.TextField(
#         null=True,
#         blank=True
#     )



