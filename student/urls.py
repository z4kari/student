from django.urls import path 

from . import views


app_name='stud'

urlpatterns=[ 
    path('login',views.login,name='login'),
    path('home',views.home,name='home')
]