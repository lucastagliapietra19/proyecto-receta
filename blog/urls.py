from django.contrib import admin
from django.urls import path
from recetas.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recetas/', index),

]
