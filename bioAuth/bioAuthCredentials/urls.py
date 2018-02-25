from django.urls import path

from bioAuthCredentials.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    #url(r'^$', HomeView.as_view(), name='home'),
    #path('', views.index, name='index'),
]