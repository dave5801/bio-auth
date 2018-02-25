from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    #url(r'^$', HomeView.as_view(), name='home'),
    #path('', views.index, name='index'),
]