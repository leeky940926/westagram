import json

from django.views      import View
from django.http       import JsonResponse

from users.utils       import login_decorator
from followings.models import Following

class FollowingView(View) :

    @login_decorator
    def post(self, request) :

        try :
            data = json.loads(request.body)
            
            #following = 내가 팔로우 하는 사람 related_name = following_giviing
            #follower  = 나를 팔로우 하는 사람 related_name = following_taking

            following_id = data['following_id']
            follower_id  = data['follower_id']

            if following_id == follower_id :
                return JsonResponse({'message':'자기자신은 팔로우 할 수 없습니다'}, status=400)

            if Following.objects.filter(follower_id=follower_id, following_id=following_id).exists() :
                Following.objects.filter(follower_id=follower_id, following_id=following_id).delete()
                return JsonResponse({'message':'follow delete'}, status=200)

            Following(
                following_id = following_id,
                follower_id  = follower_id
            ).save()

            return JsonResponse({'message':'following success'}, status=200)

        except KeyError :
            return JsonResponse({'message':'KEY_ERROR'}, status=400)