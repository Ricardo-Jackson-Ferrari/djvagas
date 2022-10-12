from django.urls import path

from . import views

app_name = 'job'

urlpatterns = [
    path('management/', views.JobManagement.as_view(), name='management'),
    path(
        'application_management/',
        views.ApplicationManagement.as_view(),
        name='application_management',
    ),
    path(
        'application/<slug:slug>',
        views.JobApplication.as_view(),
        name='application',
    ),
    path('list/', views.JobList.as_view(), name='list'),
    path('create/', views.JobCreate.as_view(), name='create'),
    path('detail/<slug:slug>', views.JobDetail.as_view(), name='detail'),
    path('delete/<slug:slug>', views.JobDelete.as_view(), name='delete'),
    path('search/', views.JobSearch.as_view(), name='search'),
]
