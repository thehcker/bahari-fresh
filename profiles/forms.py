from django import forms
from profiles.models import Profile

# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('description', 'document')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','address','description', 'image' )

class GuestForm(forms.Form):
	# class Meta:
	# 	model = GuestEmail
	# 	fields = 'email'
	email = forms.EmailField()
