from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/download/', views.download_resume, name='download_resume'),
]
