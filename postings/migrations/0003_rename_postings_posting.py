# Generated by Django 3.2.4 on 2021-09-30 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210930_1751'),
        ('postings', '0002_auto_20210930_1919'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Postings',
            new_name='Posting',
        ),
    ]