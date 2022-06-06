from django.http import HttpResponse

def index(request):
    return HttpResponse("This is a dummy rest api. Check the api endpoints: <a href=\"/api/\">Click here</a>")