from django.shortcuts import render
from .models import blogInfo

# Create your views here.

def create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        blogObj=blogInfo(title=title,content=content)
        blogObj.save()
    return render(request,'create.html')

def list(request):
    return render(request,'list.html')