from django.db import models

class TimeStampedModel(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta :
        abstract = True

class User(TimeStampedModel) :
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=500)
    name = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    other_info = models.CharField(max_length=100, null=True, blank=True)

    class Meta :
        db_table = 'users'


# class User(TimeStampedModel) :
#     #필수입력
#     identification = models.CharField(max_length=20, verbose_name='아이디', unique=True)
#     password = models.CharField(max_length=500, verbose_name='비밀번호')
#     name = models.CharField(max_length=20, verbose_name='이름')
#     email = models.EmailField(max_length=30, verbose_name='이메일', unique=True)
#     telephone = models.CharField(max_length=15, verbose_name='전화번호')
#     address1 = models.CharField(max_length=100, verbose_name='도로명주소 번지')
#     address2 = models.CharField(max_length=100, verbose_name='나머지 주소')

#     #선택입력
#     gender_menu = (
#         ('남','Man'),
#         ('여','Woman'),
#         ('선택안함',None)
#     )
#     gender = models.CharField(max_length=10, choices=gender_menu, null=True, blank=True, verbose_name='성별')

#     birthday = models.DateField(null=True, blank=True, verbose_name='생일')
#     other_info1 = models.CharField(max_length=20, null=True, blank=True, verbose_name='추천인 아이디')
#     other_info2 = models.CharField(max_length=20, null=True, blank=True, verbose_name='참여 이벤트명')

#     class Meta :
#         db_table = 'users'