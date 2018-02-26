from django.urls import path
from . import views
from bioAuthCredentials.views import HomePageView
# url(r'^$', HomeView.as_view(), name='home'),
urlpatterns = [
    #path('', views.home_view, name='home_view'),
    path('', HomePageView.as_view(), name='home'),
    #path('', views.index, name='index'),
]