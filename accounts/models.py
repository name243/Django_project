from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class Role(models.TextChoices):
        DIRECTOR = 'DIRECTOR', "Директор"
        EMPLOYEE = "EMPLOYEE", "Сотрудник"
        CLIENT = "CLIENT", "Клиент"

    Role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.CLIENT,
        verbose_name="Роль пользователя"

    )

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"