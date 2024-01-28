from django.urls import path
from .views import home_view, sign_up_insurance, pay, use_request, payment_dates_view, insurances

urlpatterns = [
    path('',home_view,name='home_url'),
    path('sign_up_insurance/<int:pk>/',sign_up_insurance,name='sign_up_insurance_url'),
    path('pay/<str:date>/<int:ins_pk>/',pay,name='pay_url'),
    path('use_request/<int:ins_pk>',use_request,name='use_request_url'),
    path('payment_dates/<int:ins_pk>',payment_dates_view,name='payment_date_url'),
    path('insurances/', insurances, name='insurances_url')
]