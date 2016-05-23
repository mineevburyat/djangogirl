from django.shortcuts import render
from .models import Agreement
# Create your views here.
def agreement_list(request):
    agreements = Agreement.objects.all()
    return render(request, 'agreement/list.html', {'agreements': agreements})