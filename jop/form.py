from dataclasses import fields
from django.forms import ModelForm
from .models import Apply, Jop


class ApplyForm(ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email', 'website', 'cv','cover_letter']


class JopForm(ModelForm):
    class Meta:
        model = Jop
        fields = '__all__'
        exclude = ('user',)
