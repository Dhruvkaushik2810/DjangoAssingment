from django import forms
from .models import ExamForm

class ExamFormForm(forms.ModelForm):
    class Meta:
        model = ExamForm
        fields = '__all__'