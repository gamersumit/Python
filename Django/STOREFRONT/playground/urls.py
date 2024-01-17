from django.urls import path
from . import views

# urlconfigration
urlpatterns = [
    path('hello/', views.say_hello),
]