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
    if request.method=='POST':
        answer_content = request.POST['answer_content']
        use_insurance1.request_answer = answer_content
        use_insurance1.save()
        return HttpResponseRedirect(reverse('consultant:my_page_cons_url',args=(consultant1.pk,)))
    else:
        return render(request,'My_page_cons.html',{'user': consultant1})