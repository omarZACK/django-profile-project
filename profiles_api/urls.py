from django.urls import path
from .views import HelloWorldView
urlpatterns =[
    path('hello-view/',HelloWorldView.as_view())
]