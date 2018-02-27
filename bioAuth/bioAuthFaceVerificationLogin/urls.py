from django.urls import path
from bioAuthFaceVerificationLogin.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]