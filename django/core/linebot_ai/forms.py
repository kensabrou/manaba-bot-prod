from django import forms
from .models import Student

class StudentEditForm(forms.ModelForm):
    manaba_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = ('manaba_id', 'manaba_password',)

        
