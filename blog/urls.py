from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from recetas.views import (index, PostDetalle, PostListar, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout, 
                               AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle, AboutListar )
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recetas/', index, name="recetas-index"),
    path('recetas/<int:pk>/detalle/', PostDetalle.as_view(), name="recetas-detalle"),
    path('recetas/listar/', PostListar.as_view(), name="recetas-listar"),
    path('recetas/crear/',PostCrear.as_view(), name="recetas-crear"),
    path('recetas/<int:pk>/borrar/',PostBorrar.as_view(), name="recetas-borrar"),
    path('recetas/<int:pk>/actualizar/',PostActualizar.as_view(), name="recetas-actualizar"),
    path('recetas/signup/', UserSignUp.as_view(), name ="recetas-signup"),
    path('recetas/login/', UserLogin.as_view(), name= "recetas-login"),
    path('recetas/logout/', UserLogout.as_view(), name="recetas-logout"),
    path('recetas/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="recetas-avatars-actualizar"),
    path('recetas/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="recetas-users-actualizar"),
    path('recetas/mensajes/crear/', MensajeCrear.as_view(), name="recetas-mensajes-crear"),
    path('recetas/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="recetas-mensajes-detalle"),
    path('recetas/mensajes/listar/', MensajeListar.as_view(), name="recetas-mensajes-listar"),
    path('recetas/about/', AboutListar.as_view(), name= "recetas-about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)