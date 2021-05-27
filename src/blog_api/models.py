from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        "Title",
        max_length=20,
        validators=RegexValidator(
            r'^[a-zA-Zа-яА-Я!?,.\s]*$',
            'Заголовок может содержать только знаки препинания, пробелы, русские и латинские символы'
        )
    )
    text = models.TextField("Text", max_length=6000)
    user = models.ForeignKey(
        User,
        related_name='posts',
        related_query_name='posts',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
