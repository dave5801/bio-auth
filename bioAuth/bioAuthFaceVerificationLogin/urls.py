from django.urls import path
from bioAuthFaceVerificationLogin.views import LoginPageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login')
]