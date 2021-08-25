from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.home, name='home_page'),
    path('<int:skill_id>/', views.detail, name='detail'),
]