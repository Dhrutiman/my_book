import requests
from requests.compat import quote_plus
from django.shortcuts import render
from . import models
from bs4 import BeautifulSoup

# Create your views here.
main_url='http://gen.lib.rus.ec/search.php?req={}&open=0&res=50&view=simple&phrase=1&column={}'
def home(request):
    return(render(request, 'book_app\home.html'))


def new_search(request):
    search= request.POST.get('search')
    search_type = request.POST.get('Search_type')

    models.Search.objects.create(search=search,type=search_type)

    url_f=main_url.format(quote_plus(search),search_type)
    response=requests.get(url_f)
    page_html=response.text

    page_data=BeautifulSoup(page_html,features='html.parser')

    post_data=page_data.find_all('tr',{'valign':'top','bgcolor':('#C6DEFF','')})

    for_front_data=[]
    check=0
    for post in post_data:

        check+=1

        ## all the required data from the page in text form ##
        book=post.find_all('td')
        book_id=book[0].text
        book_data=book[2].find('a',{'id':book_id})
        book_author=book[1].find_all('a')
        book_year=book[4].text
        book_lng=book[6].text
        book_link=book[9].find('a').get('href')
        book_formate=book[8].text

        ## to get picture of the book ##
        pic_url=book_link.split('_')
        res = requests.get(book_link)
        book_html = res.text
        picture_html = BeautifulSoup(book_html, features='html.parser')
        picture_data = picture_html.find('img',{'alt':'cover'})
        picture_url1=picture_data.get('src')
        picture_url = pic_url[0] +picture_url1

        ## go get at max three author name of the book ##
        author=""
        i=0
        for name in book_author:
            if author!="":
                author+=", "
            author=author+name.text
            i+=1
            if(i==3):
                break

        ## to get titel of the book ##
        ext=book_data.find_all('i')
        ex=""
        p=0
        for i in ext:
            p=1
            ex=ex+i.text

        book_title=book_data.text
        if p==1:
            book_name=book_title[:len(book_title)-len(ex)-1]
        else:
            book_name=book_title

        for_front_data.append((book_name,author,book_lng,book_year,book_link,book_formate,picture_url))
    checks=str(check)
    data_to_send={
        'search': search,
        'type':search_type,
        'for_front_data':for_front_data,
        'checks':checks,
    }
    return render(request,"book_app\\new_search.html",data_to_send)