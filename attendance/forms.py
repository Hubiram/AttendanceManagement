from django import forms
from .models import Attendance

class AttendanceForm(forms.Form):
    student_id = forms.IntegerField(label='Student ID')
    subject_id = forms.IntegerField(label='Subject ID')
    date = forms.DateField(label='Date')
    attended = forms.BooleanField(label='Attended')