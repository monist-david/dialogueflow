from django.urls import path
from .views import HomeView

app_name = 'webdemo'
urlpatterns = [
    path('', HomeView.as_view(), name='webdemo'),
]