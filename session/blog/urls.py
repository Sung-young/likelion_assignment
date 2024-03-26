from django.urls import path
from blog.views import home

# http://127.0.0.1:8000/blog/
urlpatterns = [
    path('', home)
]
