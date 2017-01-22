from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    # construct a dictionary to pass to the template engine as its context.
    # note the key boldmessage is the same as {{bodlmessage}} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    #Return a rendered response to send to the client.
    #We make use of the shortcut function 
    #Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)
def about(request):

    context_dict = {'myname': 'Julia Kim-Chung'}
    return render(request, 'rango/about.html', context=context_dict)

def static(request):
    context_img = 'images/rango.jpeg'
    return render(request, '/static/images/rango.jpeg', context=context_img)

def media(request):
    context_img = '/images/dog.jpeg'
    return render(request, '/media/images/dog.jpeg', context=context_img)
