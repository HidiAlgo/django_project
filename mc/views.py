from django.shortcuts import render,  redirect
from django.http import HttpResponse

from django.template import RequestContext

from .models import dataTable

# Create your views here.

def home(request):
    return render(request, 'home.html')

def addDetails(request):
    t = dataTable.objects.all()
    return render(request, 'add-details.html',{"tables":t})

def view(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        date = request.POST['date']
        state = request.POST['state']
        
        user = dataTable(name=name, email=email, phone=phone, address=address,date=date,state=state)
        user.save() 
    t = dataTable.objects.all()
    return render(request, 'view.html',{"tables":t})

def delete(request, id):
    d = dataTable.objects.get(id = id)
    d.delete()
    
    return redirect("/view")

def edit(request, id):
    d = dataTable.objects.get(id = id)
    return render(request, 'edit.html', {'d':d})

def update(request):
    if request.method == 'POST':
        id=request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        date = request.POST['date']
        state = request.POST['state']
        
        user = dataTable(id=id,name=name, email=email, phone=phone, address=address,date=date,state=state)
        user.save() 
    return redirect("/view")