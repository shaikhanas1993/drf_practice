from django.urls import include, path
from . import views

app_name = 'blog_api'


urlpatterns = [
    path('hello', views.hello, name='hello'),
]
