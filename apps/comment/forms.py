from django import forms

from mdeditor.fields import MDTextFormField


class MyCustomForm(forms.Form):
    content = MDTextFormField()
