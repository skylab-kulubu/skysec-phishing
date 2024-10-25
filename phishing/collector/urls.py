from django.urls import path
from .views import index,olta

urlpatterns = [
    path('', index, name='index'),
    path('olta/',olta,name='olta')
]
