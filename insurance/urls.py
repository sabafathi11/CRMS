
from django.urls import path
from .views import home_view, sign_up_insurance, pay

urlpatterns = [
    path('',home_view,name='home_url'),
    path('sign_up_insurance/<int:pk>/',sign_up_insurance,name='sign_up_insurance_url'),
    path('pay/<str:date>/<int:ins_pk>/',pay,name='pay_url'),

]