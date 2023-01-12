import datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods

# @require_http_methods(["GET"])

# def show(request):
#     return HttpResponse('<h1>This is HTTP GET request</h1>')

# def index(request):
#     now = datetime.datetime.now()
#     html = "<html><body><h3>Now time is %s.</h3></body></html>"%now
#     return HttpResponse(html)

# from django.template import loader
from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     template = loader.get_template('index.html')
#     name = {'Student':'Aaron'}
#     return HttpResponse(template.render(name))

def index(request):
    return render(request,'index.html')