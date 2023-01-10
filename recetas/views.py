from django.shortcuts import render
from django.views.generic import ListView, CreateView
from recetas.models import Post
from django.urls import reverse_lazy
def index(request):
    return render(request, "recetas/index.html",{} )

class PostList(ListView):
    model= Post
    template_name = "/recetas/post_list.html"

class PostCrear(CreateView):
    model = Post
    success_url =reverse_lazy("recetas-listar")
    fields = '__all__'