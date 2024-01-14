from django.shortcuts import render, get_object_or_404
from .models import Consultant

def my_page_cons(request, pk):
    user = get_object_or_404(Consultant, pk=pk)
    return render(request, 'My_page_cons.html', {'user': user})