from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from django.conf import settings
from .counting import counting
import numpy as np
import cv2
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return render(request, 'fish_counting/first_view.html', {})


def count(request):
    if request.method == 'POST':
        
        name = request.POST['name']
        id = request.POST['id']
        # imageURL = settings.MEDIA_URL + name
        # baseURL = settings.MEDIA_URL + "base.jpg"
        # cur_img = settings.MEDIA_ROOT_URL + imageURL
        # base_img = settings.MEDIA_ROOT_URL + baseURL
        res = counting(name)
        
        return HttpResponse(res)
    else:
        output = "hello"
        return HttpResponse(output)


# def dface(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()

#             imageURL = settings.MEDIA_URL + form.instance.document.name
#             opencv_dface(settings.MEDIA_ROOT_URL + imageURL)

#             return render(request, 'opencv_webapp/dface.html', {'form': form, 'post': post})
#     else:
#         form = ImageUploadForm()
#     return render(request, 'opencv_webapp/dface.html', {'form': form})




    