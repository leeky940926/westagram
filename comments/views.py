import json

from django.views    import View
from django.http     import JsonResponse

from postings.models import Posting
from users.models    import User
from comments.models import Comment
from users.utils import login_decorator

class CommentsPostView(View) :
    @login_decorator
    def post(self, request) :
        
        try :
            data = json.loads(request.body)

            posting_id = data['posting_id']
            parent_comment_id = data.get('parent_comment_id', None)
            
            if not Posting.objects.filter(id=posting_id).exists() :
                return JsonResponse({'message':'존재하지 않는 게시물입니다.'}, status=400)

            if not Comment.objects.filter(id=parent_comment_id).exists() :
                return JsonResponse({'message':'존재하지 않는 댓글입니다.'}, status=400)


            Comment(
                email_id   = data['email_id'],
                posting_id = posting_id,
                reply      = data['reply'],
                parent_comment_id = parent_comment_id
            ).save()

            return JsonResponse({'message':'댓글 등록 성공'}, status=200)
            
        except KeyError :
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        
        except json.decoder.JSONDecodeError :
            return JsonResponse({'message':'값을 제대로 입력했는지 확인해보세요'}, status=400)

        except ValueError :
            return JsonResponse({'message':'값 반환이 제대로 안됐네'}, status=400)
    
class CommentsGetView(View) :
    @login_decorator
    def get(self, request, id) :

        try :
            #id는 post의 id
            postings = Posting.objects.get(id=id)
            
            comments = postings.comment_set.all()

            result = []

            for comment in comments :

                user = User.objects.get(id=comment.email_id).email

                result.append({
                    "작성자" : user ,
                    "댓글" : comment.comment
                })
            
            return JsonResponse({'comments':result}, status=200)
        
        except TypeError as msg :
            return JsonResponse({'message':msg}, stauts=400)

    @login_decorator
    def delete(self, request, id) :
        try :
            comment_id = id

            if not Comment.objects.filter(id=comment_id).exists() :
                return JsonResponse({'message':'삭제할 수 없는 댓글입니다'}, status=400)

        except KeyError :
            return JsonResponse({'message':'KEY_ERROR'})

        Comment.objects.filter(id=comment_id).delete()
        return JsonResponse({'message':'comment delete'}, status=200)