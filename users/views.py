import bcrypt
import json
import jwt
import re


from django.http  import JsonResponse
from django.views import View
from django.utils import timezone
from datetime     import timedelta

from users.models import User

from wewe.settings import ALGORITHMS, SECRET_KEY

class SignupView(View) :
    def post(self, request) :
        try :
            data = json.loads(request.body)

            email      = data['email']
            password   = data['password']
            name       = data.get('name', None)
            telephone  = data.get('telephone', None)
            other_info = data.get('other_info', None)

            email_reg = r"^[\w+-\_.]+@[\w]+\.[\w]+$"

            if not re.match(email_reg, email) :
                return JsonResponse({'message':'Email Validation Error'}, status=401)

            password_reg = r"^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+=-])[a-zA-Z0-9!@#$%^&*()_+=-]{8,}$"

            if User.objects.filter(email=email).exists() :
                return JsonResponse({'message':'기 존재 이메일입니다.'}, status=401)

            if not re.match(password_reg, password) :
                return JsonResponse({'message':'Password Validation Error'}, status=401)
                    
            User(
                email      = email,
                name       = name,
                telephone  = telephone,
                other_info = other_info,
                password   = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            ).save()

            return JsonResponse({'message':'HIHI'}, status=201)

        except KeyError :
            return JsonResponse({'message':'KEY_ERROR'}, status=401)

        except UnboundLocalError :
            return JsonResponse({'message':'이메일/패스워드에 대한 값을 입력해주세요'}, status=401)

        except json.decoder.JSONDecodeError :
            return JsonResponse({'message':'값을 하나라도 입력하세요'})

class LoginView(View) :
    def post(self, request) :
        try :
            data = json.loads(request.body)

            email    = data['email']
            password = data['password']

            if not User.objects.filter(email=email).exists() :
                return JsonResponse({'message':'Email is not existed'}, status=401)

            db_password = User.objects.get(email=email).password

            if not bcrypt.checkpw(password.encode('utf-8'), db_password.encode('utf-8')) :
                return JsonResponse({'message':'Password is not existed'}, status=401)
            
            token = jwt.encode({'email':email, 'exp':timezone.now()+timedelta(weeks=3)}, SECRET_KEY, ALGORITHMS)

            return JsonResponse({'token':token}, status=201)

        except KeyError :
            return JsonResponse({'message':'KEY_ERROR'}, status=401)

        except NameError :
            return JsonResponse({'message':'name is not defined'}, status=401)

        except json.decoder.JSONDecodeError :
            return JsonResponse({'message':'값을 하나라도 입력하세요'})

            


        #     identification = data['identification'] #6자이상 영문 or 영문+숫자
        #     password = data['password'] #10자이상 / 영문,숫자,특수문자 최소 2개 / 동일한 숫자 3개이상 불가
        #     name = data['name']
        #     email = data['email']
        #     telephone = data['telephone']
        #     address1 = data['address1']
        #     address2 = data['address2']

        #     gender = data.get('gender',None)
        #     birthday = data.get('birthday',None)
        #     other_info1 = data.get('other_info1',None)
        #     other_info2 = data.get('other_info2',None)

        #     if len(identification < 6) :
        #         return JsonResponse({'message':'id는 6글자 이상이어야 합니다.'}) 
            
        #     if 

        # except KeyError :
        #     return JsonResponse({'message':'KEY_ERROR'}, status=401)

        # return JsonResponse({'message':'hihi'}, status=200)