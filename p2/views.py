from django.shortcuts import render
from django.http import HttpResponse
# Create
# 
# 
# 
#  your views here.
def index(request):
    my_dict={'insert_me':"hello i am from p2 app/index.html"}
    return render(request, 'p2/index.html', context=my_dict)
