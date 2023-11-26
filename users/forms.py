from django import forms


class RegistrationUserForm(forms.Form):
    username = forms.CharField(min_length=8, max_length=50)
    password = forms.CharField(min_length=8, max_length=50, widget=forms.PasswordInput())


class LoginUserForm(forms.Form):
    username = forms.CharField(min_length=8, max_length=50)
    password = forms.CharField(min_length=8, max_length=50, widget=forms.PasswordInput())