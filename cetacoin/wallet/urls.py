from django.urls import path
from .views import WalletCreationView, WalletListView, CryptoCurrenciesList

urlpatterns = [
    path('creation', WalletCreationView.as_view()),
    path('list', WalletListView.as_view()),
    path('currencies',CryptoCurrenciesList.as_view()),
]