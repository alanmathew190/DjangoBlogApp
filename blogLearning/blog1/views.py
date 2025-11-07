from django.shortcuts import render,redirect
from .models import blogInfo
from .forms import BlogForm

# Create your views here.

def create(request):
    if request.method=='POST':
        frm=BlogForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('list')
    else:
        frm=BlogForm()
    return render(request,'create.html',{'frm':frm})

def list(request):
    posts=blogInfo.objects.all()
    return render(request,'list.html',{'posts':posts})

def delete(request,id):
    instance=blogInfo.objects.get(id=id)
    instance.delete()
    blogs_set=blogInfo.objects.all()
    return render(request,'list.html',{'posts':blogs_set})    

def edit(request,id):
    instanceToBeEdited=blogInfo.objects.get(id=id)
    if request.method=='POST':
        frm=BlogForm(request.POST,instance=instanceToBeEdited)
        if frm.is_valid():
            frm.save()
            return redirect('list')
    else:
        frm=BlogForm(instance=instanceToBeEdited)
    
    return render(request,'create.html',{'frm':frm})


# title=request.POST.get('title')
        # content=request.POST.get('content')
        # blogObj=blogInfo(title=title,content=content)
        # blogObj.save()