from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home Page')


def studyroom(request):
    return HttpResponse('Study Room')


urlpatterns = {
    path('admin/', admin.site.urls),
    path('', home),
    path('studyroom/', home)
}
