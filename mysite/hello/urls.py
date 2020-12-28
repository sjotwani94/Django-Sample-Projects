from django.urls import path

from . import views

app_name = 'hello'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.hello, name='hello'),
]