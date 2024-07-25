from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'types']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'types': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'summary': 'Summary',
            'description': 'Description',
            'status': 'Status',
            'types': 'Types',
        }
        help_texts = {
            'summary': 'Enter a brief summary of the issue.',
            'description': 'Enter a detailed description of the issue (optional).',
            'status': 'Select the current status of the issue.',
            'types': 'Select one or more types related to this issue.',
        }
