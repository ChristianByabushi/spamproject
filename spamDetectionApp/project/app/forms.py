from django import forms
from .models import ModelUser, spamsMessage, Contact
class ModelUserForm(forms.ModelForm):
    class Meta:
        model = ModelUser
        fields = ['username', 'password']  

class SpamMessageForm(forms.ModelForm):
    class Meta:
        model = spamsMessage
        fields = ['contact', 'message']

class contactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email', 'number', 'subject', 'content'] 
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control border-0 bg-light px-4',
                                           'placeholder':'Nom', 'style':'height: 55px;',
                                            'type':"text"}),
            'email': forms.TextInput(attrs={'class':'form-control border-0 bg-light px-4',
                                           'placeholder':'Email', 'style':'height: 55px;',
                                            'type':"email"}), 
            'subject': forms.TextInput(attrs={'class':'form-control border-0 bg-light px-4',
                                           'placeholder':'subject', 'style':'height: 55px;',
                                            'type':"text"}),
            'content': forms.Textarea(attrs={'class':'form-control border-0 bg-light px-4 py-3',
                                            'rows':"4", 'placeholder':'Message'})
        } 