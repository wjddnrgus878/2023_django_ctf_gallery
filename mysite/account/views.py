import json
from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.db import connection
from .models import Account

def signup(request):
    msg = 'My Message'
    return render(request, 'Register.html', {'message': msg})

def signin(request):
    msg = 'My Message'
    return render(request, 'Login.html', {'message': msg})

class SignOutView(View):
    def get(self,request):
        request.session.flush()
        return redirect('/')

class SignUpView(View):
    def post(self, request):
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if email and password:
                if(Account.objects.filter(email=data['email']).exists()):
                    return HttpResponse(status=400)
                else:
                    Account(email=email, password=password).save()
                return HttpResponse(status=200)
            else:
                return JsonResponse({'message':'올바른 데이터를 제공해야 합니다.'}, status=400)
        else:
            return JsonResponse({'message':'잘못된 요청입니다.'}, status=400)

    
class SignInView(View):
    def post(self, request):
        data=json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        print(password)

        if email and password:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM accounts WHERE email = '{email}' and password = '{password}'")
                user = cursor.fetchone()
                print(user)

                if user:
                    request.session['id']=user[2]
                    request.session['is_admin']=user[1]
                    user_id = request.session.get('id')
                    print(user_id)
                    return JsonResponse({'id': user_id}, status=200)
                else:
                    return JsonResponse({'message':'등록되지 않은 이메일 입니다.'}, status=400)
        else:
            return JsonResponse({'message':'올바른 데이터를 제공해야 합니다.'}, status=400)