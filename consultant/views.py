import datetime
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect, FileResponse
from .models import Consultant
from insurance.models import Insurance
from insurance.models import Use_insurance


def my_page_cons(request, pk):
    user = get_object_or_404(Consultant, pk=pk)
    if request.method == 'POST':
        use_insurance1 = Use_insurance.objects.get(pk=request.POST['request_pk'])
        answer_content = request.POST['request_answer']
        use_insurance1.request_answer = use_insurance1.request_answer + answer_content + '/'
        if 'paid' in request.POST:
            use_insurance1.paid = True
            use_insurance1.paid_date = datetime.datetime.today()
        use_insurance1.save()
        return HttpResponseRedirect(reverse('consultant:my_page_cons_url', args=(user.pk,)))
    delayed_dates = []
    today_payments = []
    for ins in user.insurance_from_consultant.all():
        for payment_date in ins.payment_dates_from_insurance.all():
            if not payment_date.paid:
                if payment_date.date < datetime.date.today():
                    delayed_dates.append(payment_date)
                elif payment_date.date == datetime.date.today():
                    today_payments.append(payment_date)
    return render(request, 'My_page_cons.html',
                  {'user': user, 'today_payments': today_payments, 'delayed_dates': delayed_dates})


def turn_request_to_not_show(request, request_pk):
    use_insurance1 = Use_insurance.objects.get(pk=request_pk)
    consultant1 = use_insurance1.insurance.consultant
    use_insurance1.show_to_consultant = False
    use_insurance1.save()
    return HttpResponseRedirect(reverse('consultant:my_page_cons_url', args=(consultant1.pk,)))


def download_pdf(request, pk):
    use_insurance1 = Use_insurance.objects.get(pk=pk)
    pdf_file = use_insurance1.documents
    response = FileResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="documents.pdf"'
    return response


def consultant_view(request, pk):
    consultant1 = Consultant.objects.get(pk=pk)
    return render(request, 'consultant.html', {'consultant': consultant1})


def payment_dates_cons_view(request, ins_pk):
    insurance1 = Insurance.objects.get(pk=ins_pk)
    return render(request, 'Payment_dates_cons.html', {'insurance': insurance1})
