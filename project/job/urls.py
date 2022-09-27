from django.urls import path

from . import views

app_name = 'job'

urlpatterns = [
    path('list/', views.JobList.as_view(), name='list'),
    path('create/', views.JobCreate.as_view(), name='create'),
]
