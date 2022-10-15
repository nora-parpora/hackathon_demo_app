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


# ToDo Refactor common base class for User & Employer & RentComp & Mentors


class MyBaseUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 50
    LAST_NAME_MAX_LENGTH = 50
    PHONE_NUMBER_MAX_LENGTH = 20
    CITY_MAX_LENGTH = 30

    user = models.OneToOneField(MyBaseUser, related_name="profile_data", primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, blank=True, null=True)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, blank=True, null=True)
    phone = models.CharField(max_length=PHONE_NUMBER_MAX_LENGTH, null=True, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f'{self.first_name or ""} {self.last_name or ""}'

    def __str__(self):
        return f'{self.full_name}'


class Employer(models.Model):
    NAME_MAX_LENGTH = 100
    PHONE_NUMBER_MAX_LENGTH = 20
    ADDRESS_MAX_LENGTH = 200
    user = models.OneToOneField(MyBaseUser, related_name="employer_data", primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=NAME_MAX_LENGTH, blank=True, null=True)
    phone = models.CharField(max_length=PHONE_NUMBER_MAX_LENGTH, null=True, blank=True)
    address = models.TextField(max_length=ADDRESS_MAX_LENGTH, null=True, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    def __str__(self):
        return f'{self.name}'







