from django.urls import path
from .views import my_page, login_view, logout_view, signup_view, customer_view

urlpatterns = [
    path('my_page/<int:pk>/',my_page,name='my_page_url'),
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    path('Sign_up/', signup_view, name='sign_up_url'),
    path('customer/<int:pk>', customer_view, name='customer_url')
]