from django import forms

class SearchForm(forms.Form):
    search_for=forms.CharField( max_length=100, required=True)
    app_name=forms.CharField( max_length=50, required=False)