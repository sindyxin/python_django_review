from django import forms
from appTwo.models import User

class UserRegister(forms.ModelForm):
  class Meta:
    model =User
    fields = '__all__'
  # first_name = forms.CharField()
  # last_name = forms.CharField()
  # email = forms.EmailField()

  def clean(self):
    all_clean_data = super().clean()
    