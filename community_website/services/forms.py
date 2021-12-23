from django import forms
from django.forms import ModelForm
from .models import Service
from .models import User


# Create a Service Form
class ServiceForm(ModelForm):
	class Meta:
		model = Service
		fields = ('name', 'service_type', 'address', 'postal_code', 'professional', 'description', 'title_image')

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'service_type': forms.TextInput(attrs={'class':'form-control'}),
			'address': forms.TextInput(attrs={'class':'form-control'}),
			'postal_code': forms.TextInput(attrs={'class':'form-control'}),
			'professional': forms.CheckboxInput(),
			'description': forms.Textarea(attrs={}),

		}