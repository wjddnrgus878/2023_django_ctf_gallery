import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.static import serve as static_serve
from django.http import FileResponse, HttpResponse, HttpResponseForbidden
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

def download(request, filepath):
    file_path = os.path.normpath(os.path.join('media/file', filepath))
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="application/force-download")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
