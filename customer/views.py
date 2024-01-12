from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, reverse
from .models import Customer
from .forms import Customer_form
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
    else:
        form = Customer_form()
    return render(request, 'Sign_up.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        customer1 = Customer.objects.get(username=username, password=password)
        if customer1 is not None:
            login(request, customer1)
            return HttpResponseRedirect(reverse("insurance:home_url"))
    return render(request, 'Login.html')


def logout_view(request):
    logout(request)
    return render(request, 'Home.html')


def my_page(request, pk):
    user = get_object_or_404(Customer, pk=pk)
    return render(request, 'My_page.html', {'user': user})
