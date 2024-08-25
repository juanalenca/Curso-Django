from django.shortcuts import render

def index(request):
    conteudos = {
        'curso' : 'Curso de Django'
    }
    return render(request, 'index.html', conteudos) #chamada da constante

def contato(request):
    return render(request, 'contato.html')
