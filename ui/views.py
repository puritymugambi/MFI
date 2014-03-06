# Create your views here.

from django.shortcuts import render

from .models import Loan

def home(request):
    #loans = Loan.objects.all()
    loan = Loan.objects.filter(inst_id = 2)[0]
    data = {
        'upuzi': 'Mimi ni Ken',
        'loans': loan,
    }
    return render(request, 'index.html', data)
