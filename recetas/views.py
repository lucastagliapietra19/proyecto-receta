from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from recetas.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from recetas.forms import UsuarioForm
from recetas.models import Avatar, Post, Mensaje, About
from django.contrib.auth.admin import User


def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "recetas/index.html", {"posts": posts})


class PostDetalle(DetailView):
    model = Post

class PostList(LoginRequiredMixin, ListView):
    model = Post  

class PostCrear(CreateView):
    model = Post
    success_url = reverse_lazy("recetas-listar")
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("recetas-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("recetas-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('recetas-listar')


class UserLogin(LoginView):
    next_page = reverse_lazy('recetas-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('recetas-listar')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('recetas-listar')


class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('recetas-listar')


class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("recetas-mensajes-crear")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("recetas-mensajes-listar")

class  AboutListar(ListView):
    model = About