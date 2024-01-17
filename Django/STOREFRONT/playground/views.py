from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action in other languages

def say_hello(request):
    # pull data from db
    # send email etc
    #return HttpResponse('Hello World')
    x=1
    y=2
    return render(request, 'hello.html', {'name' : 'Sumit'})
