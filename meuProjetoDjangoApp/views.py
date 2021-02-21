from django.shortcuts import render
from .models import Livros

def getAllLivros(request):

    dadosLivros = Livros.objects.all()
    
    print(dadosLivros)

    return render(request,'index.html',{'livros':dadosLivros})

def getLivro(request,id):

    livro = Livros.objects.filter(id=id)

    return render(request,'index2.html',{'dadosLivro':livro})
