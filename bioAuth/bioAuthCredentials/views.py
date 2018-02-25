from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're bio auth home page.")
