from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def index(request):
    employees = Employee.objects.all()

    return render(request, 'index.html', {'employees': employees})

def add(request):
    context = {}

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        try: 
            obj = Employee(f_name=firstname, l_name=lastname)
            # this inserts a row into the database
            obj.save()
            return redirect('/')
        except ValueError as e:
            context['error'] = e
    return render(request, 'add.html', context)