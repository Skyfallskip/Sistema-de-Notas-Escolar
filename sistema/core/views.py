from django.shortcuts import render



# Create your views here.

def sobre(request):
    return render(request, 'html/sobre.html')

def home(request):
    return render(request, 'html/home.html')

def contato(request):
    return render(request, 'html/contato.html')

def ajuda(request):
    return render(request, 'html/ajuda.html')   