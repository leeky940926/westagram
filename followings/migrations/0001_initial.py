# Generated by Django 3.2.4 on 2021-10-01 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_auto_20210930_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_taking', to='users.user')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_giviing', to='users.user')),
            ],
            options={
                'db_table': 'followings',
            },
        ),
    ]