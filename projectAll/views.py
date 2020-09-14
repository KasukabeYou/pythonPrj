from django.http import HttpResponse

def todoFunc(request):
    returnObj = HttpResponse('<h1>hello world</h1>')
    return returnObj