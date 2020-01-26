from django import forms
from .models import *

class AddTags(forms.ModelForm):
    tags = forms.CharField(max_length=100)

    class Meta:
        model = Tags
        fields = "__all__"


class SearchForm(forms.ModelForm):
    class Meta:
        model = History
        fields = "__all__"

