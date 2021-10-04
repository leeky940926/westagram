import jwt

from django.http   import JsonResponse

from wewe.settings import (
    ALGORITHMS,
    SECRET_KEY
)
from users.models  import User

def login_decorator(func) :
    def wrapper(self, request, *args, **kwargs) :

        try :
            token = request.headers.get('Authorization', None)
            payload = jwt.decode(token, SECRET_KEY, ALGORITHMS)
            user = User.objects.get(email=payload['email'])
            request.user = user

        except jwt.exceptions.DecodeError :
            return JsonResponse({'message':"Invalid token type. Token must be a <class 'bytes'>"}, status=401)
        
        except jwt.ExpiredSignatureError :
            return JsonResponse({'message':"Expired Token"}, status=401)
        return func(self, request, *args, **kwargs)
    
    return wrapper