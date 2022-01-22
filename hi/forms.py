from django import forms

from .models import Visitors


class HelloForm(forms.ModelForm):
    phone_number = forms.CharField(label="Телефон", initial="+380", max_length=17)

    class Meta:
        model = Visitors
        fields = ("first_name", "last_name", "phone_number")
