# projects/forms.py

from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'quantity', 'tags', 'image_url']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-purple-400',
            'placeholder': 'Enter a catchy title…'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-purple-400',
            'rows': '4',
            'placeholder': 'Tell us all about it…'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-purple-400'
        })
        self.fields['quantity'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-purple-400',
            'min': '1'
        })
        self.fields['tags'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-purple-400',
            'placeholder': 'e.g. summer, casual, white'
        })
        self.fields['image_url'].widget.attrs.update({
            'class': 'w-full text-gray-700'
        })
