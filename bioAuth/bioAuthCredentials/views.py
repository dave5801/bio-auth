#from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):

    template_name = 'bioAuthCredentials/home.html'


#def index(request):
 #   return HttpResponse("Hello, world. You're bio auth home page.")
