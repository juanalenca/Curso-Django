from django.shortcuts import render

#adicionando a função indexe contatp para apontar para os arquivos html
def index(request):
    conteudos = { #criando um dicionaro
        'curso': 'Programação em Python - Django Framework'
    }
    return render(request, 'index.html') #chamada da constante

def contato(request):
    return render(request, 'contato.html')
