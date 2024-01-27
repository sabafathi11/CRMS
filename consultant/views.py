import datetime
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Consultant
from insurance.models import Use_insurance

def my_page_cons(request, pk):
    user = get_object_or_404(Consultant, pk=pk)
    if request.method == 'POST':
        use_insurance1 = Use_insurance.objects.get(pk=request.POST['request_pk'])
        answer_content = request.POST['request_answer']
        use_insurance1.request_answer = use_insurance1.request_answer + '/' + answer_content
        if 'paid' in request.POST:
            use_insurance1.paid = True
            use_insurance1.paid_date = datetime.datetime.today()
        use_insurance1.save()
        return HttpResponseRedirect(reverse('consultant:my_page_cons_url', args=(user.pk,)))
    return render(request, 'My_page_cons.html', {'user': user})


def turn_request_to_not_show(request, request_pk):
    use_insurance1 = Use_insurance.objects.get(pk=request_pk)
    consultant1 = use_insurance1.insurance.consultant
    use_insurance1.show_to_consultant = False
    use_insurance1.save()
    return HttpResponseRedirect(reverse('consultant:my_page_cons_url', args=(consultant1.pk,)))
