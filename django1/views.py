from django.http import HttpResponse

def ws_view(request):
    return HttpResponse("Hello, this is the ws_view.")
