from django.urls import path
from .views import RegisterView,LoginView, RegisterMinerView


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('miner', RegisterMinerView.as_view()),
]