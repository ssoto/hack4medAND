# -*- encoding: utf-8 -*-
from django import forms

class UploadDataForm(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(required=True, widget=forms.Textarea)
    data_set_file = forms.FileField(required=True)
