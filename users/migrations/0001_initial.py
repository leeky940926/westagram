# Generated by Django 3.2.4 on 2021-09-30 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('identification', models.CharField(max_length=20, verbose_name='아이디')),
                ('password', models.CharField(max_length=500, verbose_name='비밀번호')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('email', models.EmailField(max_length=30, verbose_name='이메일')),
                ('telephone', models.CharField(max_length=15, verbose_name='전화번호')),
                ('address1', models.CharField(max_length=100, verbose_name='도로명주소 번지')),
                ('adrress2', models.CharField(max_length=100, verbose_name='나머지 주소')),
                ('gender', models.CharField(blank=True, choices=[('남', 'Man'), ('여', 'Woman'), ('선택안함', None)], max_length=10, null=True, verbose_name='성별')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='생일')),
                ('other_info1', models.CharField(blank=True, max_length=20, null=True, verbose_name='추천인 아이디')),
                ('other_info2', models.CharField(blank=True, max_length=20, null=True, verbose_name='참여 이벤트명')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
