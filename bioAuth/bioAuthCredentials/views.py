from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

def home_view(request):
    template = loader.get_template("bioAuthCredentials/home.html")
    response_body = template.render()
    return HttpResponse(response_body)


#def index(request):
 #   return HttpResponse("Hello, world. You're bio auth home page.")
