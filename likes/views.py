import json

from django.http     import JsonResponse
from django.views    import View

from users.models    import User
from postings.models import Posting
from likes.models    import Like


class LikeView(View) :
    def post(self, request) :
        try :
        #email_id , posting_id
        #11번 포스팅에 9,10,11번이 좋아요 해봄

            data = json.loads(request.body)

            email_id   = data['email_id']
            posting_id = data['posting_id']

            count = Like.objects.filter(posting_id=posting_id).count()

            if Like.objects.filter(email_id=email_id, posting_id=posting_id).exists() :

                Like.objects.filter(email_id=email_id, posting_id=posting_id).delete()
 
                return JsonResponse({'message':'like delete', 'count like' : count-1}, status=200)

            Like.objects.create(
                email_id   = email_id,
                posting_id = posting_id
            )

            return JsonResponse({'message':'hihi', 'count like' : count+1}, status=200)
        
        except KeyError :
            return JsonResponse({'message':'KEYERROR'}, status=400)