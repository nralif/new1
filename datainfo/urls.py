from django.urls import path , include

from . import views


app_name = 'datainfo'
urlpatterns =[
    path('', views.homepage ,name = 'homepage')
]