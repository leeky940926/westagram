# Generated by Django 3.2.4 on 2021-09-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=30, unique=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='identification',
            field=models.CharField(max_length=20, unique=True, verbose_name='아이디'),
        ),
    ]
