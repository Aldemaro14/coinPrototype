from django.urls import path
from .views import WalletCreationView, WalletListView

urlpatterns = [
    path('creation', WalletCreationView.as_view()),
    path('list', WalletListView.as_view()),
]