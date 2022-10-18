from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('create/', views.AccountCreateView.as_view(), name='create'),
]
