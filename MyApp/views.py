from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from . models import Book_details
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import SignUpForm, LoginForm, BookForm, UpdateBookForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User Created'
            return redirect('login_view')
        else:
            msg = 'Form is not Valid'
    else:
        form = SignUpForm()
    return render(request,'register.html',{'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                msg = 'Invalid Credentials'
        else:
            msg = 'Error validating form'
    return render(request, 'registration/login.html',{'form': form, 'msg': msg})

@staff_member_required
@login_required
def add_book(request):
    if request.method == "POST":
        add_book_form = BookForm(request.POST)
        if add_book_form.is_valid():
            add_book_form.save()
            return HttpResponseRedirect('/books')
    else:
        add_book_form = BookForm()
    add_book_form = BookForm
    return render(request, 'add_books.html',{'book_form':add_book_form})

@staff_member_required
@login_required
def update_book(request, id):
    book = Book_details.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request,'updatebook.html',
    {'book': book,
    'form':form})

@staff_member_required
@login_required
def delete_book(request,id):
    record = Book_details.objects.get(id = id)
    record.delete()
    return redirect('books')

@login_required
def display_books(request):
    all_books = Book_details.objects.all()
    return render(request, 'books.html',{'books' : all_books})