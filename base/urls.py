from django.urls import path
from . import views

urlpatterns = {
    path('', views.home, name="home"),
    path('studyroom/', views.studyroom, name="Study Room "),

}
