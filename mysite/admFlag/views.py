from django.shortcuts import render

def index(request):
    msg = 'My Message'
    user_id=request.session.get('id')
    is_admin=request.session.get('is_admin',False)
    flag=get_flag() if is_admin else None
    return render(request, 'adm.html', {'id':user_id, 'flag':flag, 'is_admin':is_admin})

def get_flag():
    with open('static/txt/flag.txt', 'r') as file:
        return file.read()
