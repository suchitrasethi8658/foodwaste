from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
from .choices import * 

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )

class SignUpFormag(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', 'email', )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'weight', 'locations', 'document',)

class OrphanForm(forms.ModelForm):
    class Meta:
        model = Orphanagedetails
        fields = ('oname', 'olocation', 'totalppl', 'omobile', )
		
class AllocatingForm(forms.ModelForm):
   class Meta:
       model = Book
       fields = ('name', 'weight', 'locations', 'allocation', 'document',)