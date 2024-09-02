from Navacrotchetapp.models import Appointments
from django import forms


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['fullname','subject', 'message']
        