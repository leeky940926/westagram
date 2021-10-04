from django.db    import models
from django.db.models.deletion import SET_NULL

from users.models import TimeStampedModel


# Create your models here.
class Comment(TimeStampedModel) :
    email   = models.ForeignKey('users.User' ,on_delete=models.CASCADE)
    posting = models.ForeignKey('postings.Posting', on_delete=models.CASCADE)
    reply   = models.CharField(max_length=100)
    parent_comment = models.ForeignKey('self', on_delete=SET_NULL, null=True)

    class Meta :

        db_table = 'comments'