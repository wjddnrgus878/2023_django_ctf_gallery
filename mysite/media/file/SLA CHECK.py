import requests, json

def check_sla(url):
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False
    
def check_signup(url):
    data={
    'email':'tester4',
    'password':'testpassword'
    }
    json_data = json.dumps(data)
    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        return True
    else:
        return False

def check_signin(url):
    data={
    'email':'tester4',
    'password':'testpassword'
    }
    json_data = json.dumps(data)
    s = requests.Session()
    response = s.post(url, data=json_data, headers={'Content-Type': 'application/json'})
    response_json = response.json()
    if response.status_code == 200:
        print(response_json.get('id'))
        logout_url = "http://127.0.0.1:8000/sign/out"
        logout_response = s.get(logout_url)
        print(logout_response.status_code)
        print(s.cookies.get('id'))
        return True
    else:
        return False
    
def file_upload():
    file_path = 'C:\\Users\\wjddn\\Desktop\\test.png'
    upload_url = 'http://127.0.0.1:8000/upload'
    with open(file_path, 'rb') as file:
        files = {'document': file}
        response = requests.post(upload_url,files=files)
    print(response.status_code)
    if 'Your file name is' in response.text:
        return True
    else:  
        return False
    
def admin_check():
    data={
    'email':'tear',
    'password':'123123'
    }
    json_data = json.dumps(data)
    s = requests.Session()
    response = s.post(url, data=json_data, headers={'Content-Type': 'application/json'})
    response_json = response.json()

    adm_url='http://127.0.0.1:8000/adm'
    adm_response = s.get(adm_url)
    if 'You is not admin' in adm_response.text:
        return False
    else:
        return True
    
def not_admin_check():
    data={
    'email':'123',
    'password':'1234'
    }
    json_data = json.dumps(data)
    s = requests.Session()
    response = s.post(url, data=json_data, headers={'Content-Type': 'application/json'})
    response_json = response.json()

    adm_url='http://127.0.0.1:8000/adm'
    adm_response = s.get(adm_url)
    if 'You is not admin' in adm_response.text:
        return False
    else:
        return True



url = "http://127.0.0.1:8000/"
print(check_sla(url))
url = "http://127.0.0.1:8000/sign/up/up"
print(check_signup(url))
url = "http://127.0.0.1:8000/sign/in/in"
print(check_signin(url))
print()
#print(file_upload())
print()
print(admin_check())