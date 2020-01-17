from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_search',views.new_search, name='new_search'),
    path('book_page',views.book_page, name='book_page'),


]