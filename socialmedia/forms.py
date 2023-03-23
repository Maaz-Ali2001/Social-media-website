from django import forms

from .models import User,Credential

class ImageForm(forms.ModelForm):
    class Meta:
        model= User
        fields= ['post']