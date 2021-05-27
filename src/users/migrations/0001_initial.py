# Generated by Django 3.2.3 on 2021-05-26 14:06

from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Date deleted')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super Admin')),
                ('date_joined', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'users',
                'verbose_name_plural': 'users',
                'permissions': [('change_user_accounts', 'Change users account')],
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
                'default_permissions': [],
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
