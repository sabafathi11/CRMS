from django.urls import path
from .views import my_page_cons, turn_request_to_not_show, download_pdf, consultant_view, payment_dates_cons_view

urlpatterns = [
    path('my_page_cons/<int:pk>/',my_page_cons,name='my_page_cons_url'),
    path('turn_request_to_not_show/<int:request_pk>/',turn_request_to_not_show,name='turn_request_to_not_show_url'),
    path('download_documents/<int:pk>/', download_pdf, name='download_pdf'),
    path('consultant/<int:pk>/', consultant_view, name='consultant_url'),
    path('payment_dates_cons/<int:ins_pk>/', payment_dates_cons_view, name='payment_dates_cons_url')
]
