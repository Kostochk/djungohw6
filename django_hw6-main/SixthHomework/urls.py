from django.urls import path
from . import views

urlpatterns = [
    path('greeting/', views.greeting_view),
    path('primes/', views.prime_numbers_view),
    path('subscribe/', views.subscribe_view),
    path('multiply/', views.mult_table_range_view),
]