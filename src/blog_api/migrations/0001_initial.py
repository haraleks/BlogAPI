# Generated by Django 3.2.3 on 2021-05-27 14:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-Я!?,.\\s]*$', 'Заголовок может содержать только знаки препинания, пробелы, русские и латинские символы')], verbose_name='Title')),
                ('text', models.TextField(max_length=6000, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
