from django import forms

from url_shortener.shortener.models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["url"]
        widgets = {
            "url": forms.URLInput(
                attrs={
                    "type": "url",
                    "class": "url-form-input form-component",
                    "placeholder": "Enter the link here",
                }
            )
        }
