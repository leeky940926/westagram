from django.db    import models

from users.models import TimeStampedModel

class Following(TimeStampedModel) :

    following = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='following_giviing')
    follower  = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='following_taking')

    class Meta :
        
        db_table = 'followings'