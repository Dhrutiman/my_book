import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return(render(request, 'book_app\home.html'))

def new_search(request):
    search= request.POST.get('search')
    search_type = request.POST.get('Search_type')
    #print(search,search_type)
    data_to_send={
        'search': search,
        'type':search_type,
    }
    return render(request,"book_app\\new_search.html",data_to_send)