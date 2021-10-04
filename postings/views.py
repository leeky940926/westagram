import json

from django.http     import JsonResponse
from django.views    import View

from users.utils     import login_decorator
from postings.models import Posting
from postings.models import Image
from users.models    import User

class PostingView(View) :
    
    @login_decorator
    def post(self, request) :
        #Posting : content
        #Image   : img_url
        try :
            data = json.loads(request.body)

            email_id   = request.user.id
            img_url = data.get('img_url', None)
            content = data.get('content', None)

            posting = Posting.objects.create(
                email_id = email_id,
                content  = content
            )

            if img_url :
                for imgs in img_url :
                    Image.objects.create(
                        posting_id = posting.id,
                        img_url    = imgs
                    )
                    
        except KeyError :
            return JsonResponse({'message':'KEY_ERROR'}, status=401)

        except json.decoder.JSONDecodeError :
            return JsonResponse({'message':'값을 하나라도 입력하세요'}, status=401)

        return JsonResponse({'message':'Success'}, status=200)

    @login_decorator
    def get(self, request) :
        #등록된 모든 게시물 / 등록한 사람, 등록한 시간, 게시물url, 게시물 내용

        try :
            postings = Posting.objects.all()

            result = []

            for posting in postings :

                img_url = posting.image_set.all()
                
                url_list = []

                for urls in img_url :

                    url_list.append({
                        'url_list' : urls.img_url
                    })
        
                result.append(
                    {
                        '등록한 사람' : User.objects.get(id=posting.email_id).email,
                        '등록한 시간' : posting.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                        '게시물 url' : url_list,
                        '게시물 내용' : posting.content
                    }
                )

            return JsonResponse({'message':result}, status=201)
        
        except AttributeError as msg :
            return JsonResponse({'message':msg}, stauts=400)
        
        except TypeError as msg :
            return JsonResponse({'message':msg}, stauts=400)

    @login_decorator
    def delete(self, request, id) :
        try :
            posting_id = id

            if not Posting.objects.filter(id=posting_id).exists() :
                return JsonResponse({'message':'Posting is already not existed'}, status=400)

        except KeyError :
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        
        Posting.objects.filter(id=posting_id).delete()

        return JsonResponse({'message':'delete ok'}, status=200)

class PostingUpdateView(View) :
    @login_decorator
    def post(self, request, id) :
        
        try :
            #content => Posting
            #img_url => Image

            data = json.loads(request.body)

            posting_id = id

            posting = Posting.objects.get(id=posting_id)
            image   = Image.objects.filter(posting_id=posting_id)

            content = data.get('content', posting.content)
            img_url = data.get('img_url', image)

            Posting.objects.filter(id=posting_id).update(content = content)

            if img_url :

                Image.objects.filter(posting_id=posting_id).delete()

                for url in img_url :
                
                    Image.objects.create(
                        img_url = url,
                        posting = posting
                    )
            
            return JsonResponse({'message':'update good'}, status=200)

        except KeyError :
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except json.decoder.JSONDecodeError:
            return JsonResponse({'message':'Json Decode Error'}, status=500)