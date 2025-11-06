from  django.forms import ModelForm
from .models import blogInfo

class BlogForm(ModelForm):
    class Meta:
        model=blogInfo
        fields= '__all__'