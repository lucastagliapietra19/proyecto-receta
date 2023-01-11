from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from recetas.views import (index, PostList, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout, 
                               AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle )
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recetas/', index, name="recetas-index"),
    path("recetas/listar/",PostList.as_view(), name="recetas-listar"),
    path('recetas/crear/',PostCrear.as_view(), name="recetas-crear"),
    path('recetas/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="recetas-borrar"),
    path('recetas/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="recetas-actualizar"),
    path('recetas/signup/', UserSignUp.as_view(), name ="recetas-signup"),
    path('recetas/login/', UserLogin.as_view(), name= "recetas-login"),
    path('recetas/logout/', UserLogout.as_view(), name="recetas-dos-logout"),
    path('recetas/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="recetas-avatars-actualizar"),
    path('recetas/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="recetas-users-actualizar"),
    path('recetas/mensajes/crear/', MensajeCrear.as_view(), name="recetas-mensajes-crear"),
    path('recetas/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="recetas-mensajes-detalle"),
    path('recetas/mensajes/listar/', MensajeListar.as_view(), name="recetas-mensajes-listar"),
]
