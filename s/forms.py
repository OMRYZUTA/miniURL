from django import forms


class Url(forms.Form):
    #for original url
    url = forms.CharField(label="URL") 
