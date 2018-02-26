from django.urls import path
from bioAuthCredentials.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]