from django.contrib import admin
from django.urls import path
from recetas.views import index, PostList, PostCrear

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recetas/', index, name="recetas-index"),
    path("recetas/listar/",PostList.as_view(), name="recetas-listar"),
    path('recetas/crear/',PostCrear.as_view(), name="recetas-crear"),

]
