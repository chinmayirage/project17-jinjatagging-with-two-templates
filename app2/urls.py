from django.urls import path
from app2.views import *
app2_name='something1'
urlpatterns=[
    path('second/',second,name='second.html'),
]
