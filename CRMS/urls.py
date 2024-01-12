
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('consultant.urls','consultant'),namespace='consultant')),
    path('',include(('customer.urls','customer'),namespace='customer')),
    path('',include(('insurance.urls','insurance'),namespace='insurance'))
]
