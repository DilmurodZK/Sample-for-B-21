from django.urls import path
from .views import *

urlpatterns = [
    path('api/', get_data),
    path('api/create-book/', create_book),
    path('api/update-book/<int:pk>/', update_book),
    path('api/get-book/<int:pk>/', get_book),
    path('api/search-book/', search_book)
]