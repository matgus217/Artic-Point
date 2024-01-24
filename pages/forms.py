from django.forms import ModelForm
from django import forms
from .models import Reservation

tableChoices = {
    'window1': 'Table with view',
    'window2': 'Table around ice-fountain',
    'bigTable1': 'Big table with lake view',
    'bigTable2': 'Big table upstairs with lake view'
}

sittingTimes = [('3-5', '15-17'), ('5-7', '17-19'), ('7-9', '19-21'),]


class Reserve_table_form(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Full Name', 'style': 'width: 200px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'style': 'width: 200px;', 'class': 'form-control'}))
    phone_number = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': 'Phone-number', 'style': 'width: 200px;', 'class': 'form-control'}))
    number_of_people = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Number of people', 'style': 'width: 200px;', 'class': 'form-control'}))
    date = forms.DateField(widget=forms.NumberInput(
        attrs={'placeholder': 'Which day do you wish to visit us?', 'class': 'form-control', 'type': 'date', 'style': 'width: 200px;'}))
    time = forms.ChoiceField(choices=sittingTimes, widget=forms.Select(
        attrs={'placeholder': 'What time do you want to visit us?', 'style': 'width: 200px;', 'class': 'form-control'}))

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone_number',
                  'number_of_people', 'date', 'time']
