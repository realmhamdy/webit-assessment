from django import forms

from python_test.models import Client


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ("name", "email", "phone")


class ClientSearchForm(forms.Form):

    name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    suburb = forms.CharField(required=False)
    order_by = forms.ChoiceField(choices=(("name", "Name"), ("email", "Email"), ("phone", "Phone"), ("address__suburb", "Suburb")), required=False)

    class Meta:
        fields = ("name", "email", "phone", "suburb", "order_by")
