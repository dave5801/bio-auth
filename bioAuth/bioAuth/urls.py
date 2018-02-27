"""bioAuth URL Configuration."""


from django.contrib import admin
from django.urls import path
from bioAuth.views import HomePageView
import bioAuthFaceVerificationLogin.views 


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', bioAuthFaceVerificationLogin.views, name='login'),
    path('admin/', admin.site.urls),

]
