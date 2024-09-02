from django.shortcuts import render, redirect
from Navacrotchetapp.models import Appointments
from Navacrotchetapp.form import AppointmentForm


# Create your views here.
def portfolio(request):
    return render(request, 'portfolio-details.html')


def index(request):
    return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def Appoints(request):
    myappointments = Appointments.objects.all()
    return render(request, 'Appoints.html', {'Appointments': myappointments})


def appointment(request):
    if request.method == 'POST':
        appointments = Appointments(
            fullname=request.POST['fullname'],
            message=request.POST['message'],
            subject=request.POST['subject'],
        )
        appointments.save()
        return redirect("/Appoints")
    else:
        return render(request, 'appointment.html')
def delete(request,id):
    myappointment = Appointments.objects.get(id=id)
    myappointment.delete()
    return redirect("/Appoints")
def edit(request,id):
    editappointment= Appointments.objects.get(id=id)
    return render(request,'edit.html',{'appointments':editappointment})
def update(request,id):
    updateinfo= Appointments.objects.get(id=id)
    form = AppointmentForm(request.POST,instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/Appoints')
    else:
        return render(request,'edit.html')



