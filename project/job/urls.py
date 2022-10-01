from django.urls import path

from . import views

app_name = 'job'

urlpatterns = [
    path('management/', views.JobManagement.as_view(), name='management'),
    path('list/', views.JobList.as_view(), name='list'),
    path('create/', views.JobCreate.as_view(), name='create'),
    path('detail/<slug:slug>', views.JobDetail.as_view(), name='detail'),
    path('delete/<slug:slug>', views.JobDelete.as_view(), name='delete'),
]
