# Generated by Django 3.2.4 on 2021-09-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postings',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='postings',
            name='img_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
