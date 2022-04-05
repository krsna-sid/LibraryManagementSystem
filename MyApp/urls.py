from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/', views.register, name='register'),
    path('add_book/',views.add_book,name='add-book'),
    path('books/',views.display_books,name='books'),
    path('update/<int:id>',views.update_book, name='update-books'),
    path('delete/<int:id>', views.delete_book, name='delete-book'),
    ]    
