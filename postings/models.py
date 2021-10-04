from django.db import models

from users.models import TimeStampedModel

class Posting(TimeStampedModel) :
    email   = models.ForeignKey('users.User' ,on_delete=models.CASCADE)
    content = models.TextField(max_length=500, null=True, blank=True)

    class Meta :
        db_table = 'postings'

class Image(TimeStampedModel) :
    img_url = models.CharField(max_length=500, null=True, blank=True)
    posting = models.ForeignKey('Posting', on_delete=models.CASCADE)

    class Meta :
        db_table = 'images'