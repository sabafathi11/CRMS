import datetime
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, reverse
from .models import Customer
from django.http import HttpResponseRedirect


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        natural_number = request.POST['natural_number']
        customer1 = Customer.objects.create(username=username, password=password, first_name=first_name,
                                            last_name=last_name, phone_number=phone_number, address=address,
                                            natural_number=natural_number)
        customer1.save()
        return HttpResponseRedirect(reverse("customer:login_url"))
    return render(request, 'Sign_up.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            customer1 = Customer.objects.get(username=username, password=password)
        except:
            customer1 = None
        if customer1 is not None:
            login(request, customer1)
            if customer1.kind == '1':
                return HttpResponseRedirect(reverse("customer:my_page_url", args=(customer1.pk,)))
            else:
                return HttpResponseRedirect(reverse("consultant:my_page_cons_url", args=(customer1.pk,)))
        else:
            return HttpResponseRedirect(reverse('customer:login_url'))
    return render(request, 'Login.html')


def logout_view(request):
    logout(request)
    return render(request, 'Home.html')


def my_page(request, pk):
    user = get_object_or_404(Customer, pk=pk)
    insurances = user.insurance_from_customer.all()
    payment_dates = []
    delayed_dates = []
    for ins in insurances:
        for payment_date in ins.payment_dates_from_insurance.all():
            if not payment_date.paid:
                if payment_date.date >= datetime.date.today():
                    payment_dates.append([payment_date, payment_date.date])
                if payment_date.date < datetime.date.today():
                    delayed_dates.append(payment_date)
    payment_dates.sort(key=lambda l: l[1])
    try:
        closest_payment = payment_dates[0][0]
    except:
        closest_payment = ''
    return render(request, 'My_page.html',
                  {'user': user, 'closest_payment': closest_payment, 'delayed_dates': delayed_dates})


def customer_view(request, pk):
    customer1 = Customer.objects.get(pk=pk)
    return render(request, 'customer.html', {'customer': customer1})