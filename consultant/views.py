import datetime
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Consultant
from insurance.models import Use_insurance


def my_page_cons(request, pk):
    user = get_object_or_404(Consultant, pk=pk)
    return render(request, 'My_page_cons.html', {'user': user})


def answer_use_request(request, request_pk):
    use_insurance1 = Use_insurance.objects.get(pk=request_pk)
    consultant1 = use_insurance1.insurance.consultant
    if request.method == 'POST':
        answer_content = request.POST['answer_content']
        use_insurance1.request_answer = answer_content
        use_insurance1.save()
        return HttpResponseRedirect(reverse('consultant:my_page_cons_url', args=(consultant1.pk,)))
    else:
        return render(request, 'Answer_use_request.html', {'use_insurance': use_insurance1})


def turn_request_to_paid(request, request_pk):
    use_insurance1 = Use_insurance.objects.get(pk=request_pk)
    consultant1 = use_insurance1.insurance.consultant
    use_insurance1.paid = True
    paid_date = datetime.date.today()
    use_insurance1.paid_date = paid_date
    use_insurance1.save()
    return HttpResponseRedirect(reverse('consultant:my_page_cons_url', args=(consultant1.pk,)))


def turn_request_to_not_show(request, request_pk):
    use_insurance1 = Use_insurance.objects.get(pk=request_pk)
    consultant1 = use_insurance1.insurance.consultant
    use_insurance1.show_to_consultant = False
    use_insurance1.save()
    return HttpResponseRedirect(reverse('consultant:my_page_cons_url', args=(consultant1.pk,)))
