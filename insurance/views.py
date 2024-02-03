import datetime
from django.shortcuts import render, reverse
from .models import Insurance, Payment_dates, Customer, Bank_card, Use_insurance
from django.http import HttpResponseRedirect


def home_view(request):
    return render(request, 'Home.html')


def sign_up_insurance(request, pk):
    cost_per_year = Insurance.cost_per_year
    if request.method == 'POST':
        name = request.POST['name']
        created_at = datetime.date.today()
        duration = request.POST['duration']
        payment_kind = request.POST['payment_kind']
        insurance1 = Insurance.objects.create(name=name, customer_id=pk, created_at=created_at, duration=duration,
                                              cost=cost_per_year[int(name)] * int(duration), payment_kind=payment_kind)
        insurance1.save()
        if payment_kind == '2':
            month = created_at.month
            year = created_at.year
            for i in range(int(insurance1.payment_count)):
                payment_date1 = Payment_dates(date=created_at.replace(month=month, year=year), insurance=insurance1)
                payment_date1.save()
                month += 1
                if month == 13:
                    month = 1
                    year += 1
        else:
            year = created_at.year
            for i in range(int(insurance1.payment_count)):
                payment_date1 = Payment_dates(date=created_at.replace(year=year), insurance=insurance1)
                payment_date1.save()
                year += 1
        return HttpResponseRedirect(reverse("customer:my_page_url", args=(pk,)))
    return render(request, 'Sign_up_insurance.html')


def pay(request, date, ins_pk):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    payment1 = Payment_dates.objects.get(insurance_id=ins_pk, date=date)
    payment1.paid = True
    payment1.paid_date = datetime.datetime.today()
    payment1.save()
    return HttpResponseRedirect(reverse("insurance:payment_date_url", args=(ins_pk,)))


def use_request(request, ins_pk):
    if request.method == 'POST':
        card_number = request.POST['card_number']
        shaba_number = request.POST['shaba_number']
        bank_name = request.POST['bank_name']
        owner_pk = Insurance.objects.get(pk=ins_pk).customer.pk
        recieve_card = Bank_card.objects.create(card_number=card_number, shaba_number=shaba_number, bank_name=bank_name,
                                                owner_id=owner_pk)
        recieve_card.save()
        recieve_card_pk = recieve_card.pk
        request_content = request.POST['request_content']
        request_date = datetime.date.today()
        amount = request.POST['amount']
        documents = request.POST['documents']
        use_insurance1 = Use_insurance.objects.create(request_content=request_content, request_date=request_date,
                                                      amount=amount, recieve_card_id=recieve_card_pk,
                                                      documents=documents,
                                                      insurance_id=ins_pk)
        use_insurance1.save()
        return HttpResponseRedirect(reverse('customer:my_page_url', args=(owner_pk,)))
    else:
        return render(request, 'Use_insurance_request.html')


def payment_dates_view(request, ins_pk):
    insurance1 = Insurance.objects.get(pk=ins_pk)
    return render(request, 'Payment_dates.html', {'insurance': insurance1})


def insurances(request):
    return render(request, 'insurances.html')