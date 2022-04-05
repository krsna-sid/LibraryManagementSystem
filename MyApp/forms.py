from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User, Book_details
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','gender','is_student')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)



class BookForm(ModelForm):
    publication_yr = forms.DateField(widget = forms.SelectDateWidget(years=range(1900,2023)))
    class Meta:
        model = Book_details
        fields = ('book_title','language','publication_by','publication_yr','category','shelf_name','copies_actual','copies_current')
        labels = {
        "book_title": "Title of the book",
        "language": "Language",
        "publication_by": "Published By",
        "publication_yr": "Published Year",
        "category": "Category",
        "shelf_name": "Shelf Details",
        "copies_actual": "Total Copies",
        "copies_current":"Available Copies"
        }

class UpdateBookForm(ModelForm):
    publication_yr = forms.DateField(widget = forms.SelectDateWidget)
    class Meta:
        model = Book_details
        fields = ('book_title','language','publication_by','publication_yr','category','shelf_name','copies_actual','copies_current')
        labels = {
        "book_title": "",
        "language": "",
        "publication_by": "",
        "publication_yr": "Publication Year",
        "category": "",
        "shelf_name": "",
        "copies_actual": "",
        "copies_current":""
        }