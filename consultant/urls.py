from django.urls import path
from .views import my_page_cons, turn_request_to_not_show

urlpatterns = [
    path('my_page_cons/<int:pk>/',my_page_cons,name='my_page_cons_url'),
    path('turn_request_to_not_show/<int:request_pk>/',turn_request_to_not_show,name='turn_request_to_not_show_url'),
]
