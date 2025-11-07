from django.urls import path
from .import views

urlpatterns = [
    path('create/',views.create,name='create'),
    path('list/',views.list,name='list'),
    path('delete/<id>',views.delete,name='delete'),
    path('edit/<id>',views.edit,name='edit')

    
]