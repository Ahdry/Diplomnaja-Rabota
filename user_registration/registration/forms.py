from django import forms

class RegistrationForm(forms.Form):
    num_users = forms.IntegerField(label='Количество пользователей', min_value=1)