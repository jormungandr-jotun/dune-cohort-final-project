from django import forms
from .models import Property, Inquiry

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ("owner", "created_at", "updated_at")
        widgets = {"description": forms.Textarea(attrs={"rows": 5})}

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ("message",)
        widgets = {"message": forms.Textarea(attrs={"rows": 4})}
