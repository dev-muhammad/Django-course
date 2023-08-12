from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class CustomUserManager(UserManager):
    
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    nickname = models.CharField("Никнейм", max_length=50, unique=True)
    email = models.EmailField("Почта", unique=True)
    phone = models.CharField("Телефон", max_length=12, null=True, blank=True)
    name = models.CharField("Имя", max_length=50)
    avatar = models.ImageField("Фото", upload_to="users/avatar", null=True, blank=True)

    create_time = models.DateTimeField("Время создания", auto_now_add=True)
    update_time = models.DateTimeField("Время обновления", auto_now=True)
    
    is_active = models.BooleanField("Активный", default=True)
    is_superuser = models.BooleanField("Супер пользователь", default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return f"({self.id}) {self.nickname}"
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def save(self, *args, **kwargs) -> None:
        self.nickname = self.email[:self.email.index("@")]
        return super().save(*args, **kwargs)   

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
