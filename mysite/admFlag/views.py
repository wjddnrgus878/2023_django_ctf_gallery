from django.shortcuts import render

def index(request):
    msg = 'My Message'
    user_id=request.session.get('id')
    flag=get_flag()
    return render(request, 'adm.html', {'id':user_id, 'flag':flag})

def get_flag():
    with open('static/txt/flag.txt', 'r') as file:
        return file.read()
