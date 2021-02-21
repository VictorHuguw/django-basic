
from django.contrib import admin
from django.urls import path
from .views import getAllLivros,getLivro

urlpatterns = [
    path('', getAllLivros,name="index"),
    path('livro/<int:id>', getLivro,name="livro"),
]
