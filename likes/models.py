from django.db import models

from users.models import TimeStampedModel

class Like(TimeStampedModel) :
    posting = models.ForeignKey('postings.Posting', on_delete=models.CASCADE)
    email   = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta :
        db_table = 'likes'