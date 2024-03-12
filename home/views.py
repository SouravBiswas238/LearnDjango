from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        "variable1" : "new variable send",
        "variable2" : "new variable sourav",
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services")

def contract(request):
    return HttpResponse("This is contract")

def other(request):
    return HttpResponse("This is other")
