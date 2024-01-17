import datetime
from django.shortcuts import render, reverse
from .forms import Insurance_form
from .models import Insurance, Payment_dates, Customer
from django.http import HttpResponseRedirect

cost_per_year = {1: 300000,
                 2: 400000,
                 3: 500000,
                 4: 300000,
                 5: 200000,
                 6: 250000,
                 7: 600000,
                 8: 600000,
                 9: 500000,
                 10: 80000}


def home_view(request):
    return render(request, 'Home.html')


def sign_up_insurance(request, pk):
    if request.method == 'POST':
        name = request.POST['name']
        created_at = datetime.date.today()
        duration = request.POST['duration']
        payment_kind = request.POST['payment_kind']
        insurance1 = Insurance.objects.create(name=name, customer_id=pk, created_at=created_at, duration=duration,
                                              cost=cost_per_year[int(name)] * int(duration), payment_kind=payment_kind)
        insurance1.save()
        j=0
        i=0
        while j< int(insurance1.payment_count):
            if payment_kind == '1':
                if i==12:
                    i=1
                payment_date1 = Payment_dates(date=created_at.replace(month=(created_at.month + i) % 12),
                                              insurance=insurance1)
            else:
                payment_date1 = Payment_dates(date=created_at.replace(year=created_at.year + i), insurance=insurance1)
            payment_date1.save()
            j+=1
            i+=1

        return HttpResponseRedirect(reverse("customer:my_page_url", args=(pk,)))
    else:
        form = Insurance_form()
    return render(request, 'Sign_up_insurance.html', {'form': form})

def pay(request,date,ins_pk):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    payment1 = Payment_dates.objects.get(insurance_id=ins_pk,date=date)
    user_pk = Insurance.objects.get(pk=ins_pk).customer.pk
    payment1.paid = True
    payment1.save()
    return HttpResponseRedirect(reverse("customer:my_page_url", args=(user_pk,)))

def use(request):
    pass