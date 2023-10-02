from django.shortcuts import render
from bookstore.models import BookInfo

# Create your views here.

def homepage(request):
    books = None 
    if request.user.is_authenticated:
        user = request.user 
        books = BookInfo.objects.filter(department=user.profile.department)[:10]
    else:
         books = BookInfo.objects.all()[:10]

    
    return render(request,"index.html",{"page":"home","books":books})


def aboutpage(request):
    return 