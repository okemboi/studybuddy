
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
def home(requests):
    return HttpResponse('Home Page')

def home ()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
