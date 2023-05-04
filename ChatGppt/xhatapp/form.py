from django import forms
from djagno.contrib.auth.models import User
from xhatapp.models import SaveQueries

class usserform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')