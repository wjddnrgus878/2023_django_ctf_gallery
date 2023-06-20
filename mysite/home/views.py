from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from PIL import Image

def file_upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage(location='media/file/')
        name = fs.save(uploaded_file.name, uploaded_file)
        file_name = uploaded_file.name
        print(uploaded_file.name)
    return render(request, 'index.html', {'file_name':file_name})

def index(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})

def download(request, filename):
    fs = FileSystemStorage(location='media/file/')
    file_path = fs.path(filename)
    return FileResponse(open(file_path, 'rb'), as_attachment=True)