from django.urls import path
from .views import index,delete_record,olta

urlpatterns = [
    path('', index, name='index'),
    path('delete/',delete_record,name='delete_record'),
    path('olta/',olta,name='olta')
]
