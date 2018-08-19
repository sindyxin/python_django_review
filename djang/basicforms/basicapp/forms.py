from django import forms
from django.core import validators


# def check_for_z(value):
#   if value[0].lower() != 'z':
#     raise forms.ValidationError("Name need to start with Z")

class FormName(forms.Form):
  # name = forms.CharField(validators=[check_for_z])
  name = forms.CharField()
  email = forms.EmailField(required=True)
  verify_email = forms.EmailField(label="Enter your email again")
  text = forms.CharField(widget=forms.Textarea)
  # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

  def clean(self):
    all_clean_data = super().clean()
    email =all_clean_data['email']
    v_email = all_clean_data['verify_email']

    if email != v_email:
      raise forms.ValidationError("Make sure  email match!")