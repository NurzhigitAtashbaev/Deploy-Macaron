# Generated by Django 4.1.5 on 2023-02-01 15:39

import account.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('number', models.DecimalField(decimal_places=0, max_digits=15, null=True, unique=True, verbose_name='number phone')),
                ('username', models.CharField(blank=True, default='None', max_length=220, verbose_name='username')),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treted as active.Unselect this instead of deleting accounts.', verbose_name='active')),
                ('is_superuser', models.BooleanField(blank=True, verbose_name='status')),
                ('activation_code', models.CharField(blank=True, max_length=220)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
    ]
