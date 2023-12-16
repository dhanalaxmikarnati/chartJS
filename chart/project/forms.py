from django import forms
from . models import Dashboard


class  DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = '__all__'
        widges = {
            'sector': forms.TextInput(attrs={'class':'form-control'}),
            'topic': forms.TextInput(attrs={'class':'form-control'}),
            'end_year': forms.TextInput(attrs={'class':'form-control'}),
            'region': forms.TextInput(attrs={'class':'form-control'}),
            'source': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'intensity': forms.NumberInput(attrs={'class':'form-control'}),
            'relevance': forms.NumberInput(attrs={'class':'form-control'}),      
        }