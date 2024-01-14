from django.urls import path
from .views import my_page_cons

urlpatterns = [
    path('my_page_cons/<int:pk>/',my_page_cons,name='my_page_cons'),
]
