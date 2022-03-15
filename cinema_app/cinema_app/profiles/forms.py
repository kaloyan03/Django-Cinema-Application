from django import forms

from cinema_app.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'input-field', 'placeholder': 'Your first name...'},
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'input-field', 'placeholder': 'Your last name...'},
            ),
            'age': forms.NumberInput(
                attrs={'class': 'input-field', 'placeholder': 'Your age...'},
            ),
            'profile_picture': forms.FileInput(
                attrs={'class': 'input-field'},
            ),
        }

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.user = self.user

        if commit:
            profile.save()

        return profile
