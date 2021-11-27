from django.urls import path
from . import views

app_name="posts"
urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.personal, name='personal')
]