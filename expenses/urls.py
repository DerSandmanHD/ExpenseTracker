# in expenses/urls.py

from django.urls import path
from .views import add_income

urlpatterns = [
    path('add_income/', add_income, name='add_income'),
    # weitere URLs hinzufügen, wenn nötig
]
