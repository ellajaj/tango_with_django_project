from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #construct a dictionary to pass to the template engine as its context
    #note the key boldmessage matches to {{boldmessage}}
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    #return a rendered response to send to the client.
    #We make use of the shortcut function to make out lives easier.
    #note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html',context=context_dict)

def about(request):
    return render(request, 'rango/about.html')
