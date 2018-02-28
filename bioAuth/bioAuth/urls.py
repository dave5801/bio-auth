"""bioAuth URL Configuration."""


from django.contrib import admin
from django.urls import path
from bioAuth.views import HomePageView
from bioAuthFaceVerificationLogin.views import LoginPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('admin/', admin.site.urls),

]
