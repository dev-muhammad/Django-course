from django.core.validators import MinLengthValidator
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from rest_framework.authtoken.models import Token


def digit_only(value): 
    if value.isdigit()==False:
        raise ValidationError('Digits only')


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create(self, **kwargs):
        """
        Overriding create to create Token for new created user
        """
        user = super().create(**kwargs)
        #Token.objects.get_or_create(user=user)
        return user
    
    def create_user(self, nickname, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        user = self.model(nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save()
        #Token.objects.get_or_create(user=user)
        return user
    
    def create_superuser(self, nickname, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        if password is None:
            raise TypeError('Superusers must have a password.')
        
        user = self.create_user(nickname, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser):

    class GENDER(models.IntegerChoices):
        NOT_SELECTED = 0, "Не указано"
        MALE = 1, "Mужской"
        FEMALE = 2, "Женский"

    phone = models.CharField("Номер телефона", unique=True, null=True, blank=True, max_length=12, validators=[digit_only, MinLengthValidator(10)])
    email = models.EmailField("Почта", max_length=70, unique=True, null=True, blank=True)
    nickname = models.CharField("Никнейм", max_length=70, unique=True)
    avatar = models.ImageField("Аватар", upload_to='avatars', null=True, blank=True)
    name = models.CharField("Имя", max_length=70, null=True, blank=True)
    bio = models.TextField("Обо мне", null=True, blank=True, max_length=512)
    gender = models.PositiveSmallIntegerField("Пол", choices=GENDER.choices, default=GENDER.NOT_SELECTED)

    is_active = models.BooleanField("Активный", default=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'nickname'
    #REQUIRED_FIELDS = ['']

    objects = UserManager()

    def __str__(self):
        return f"({self.id}) {self.nickname}"
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

