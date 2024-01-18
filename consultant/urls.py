from django.urls import path
from .views import my_page_cons, answer_use_request, turn_request_to_paid, turn_request_to_not_show

urlpatterns = [
    path('my_page_cons/<int:pk>/',my_page_cons,name='my_page_cons_url'),
    path('answer_use_request/<int:request_pk>/',answer_use_request,name='answer_use_request_url'),
    path('turn_request_to_paid/<int:request_pk>/',turn_request_to_paid,name='turn_request_to_paid_url'),
    path('turn_request_to_not_show/<int:request_pk>/',turn_request_to_not_show,name='turn_request_to_not_show_url'),
]
