from django import forms

from cinema_app.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    class Meta:
        model = Profile
        exclude = ['user']

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.user = self.user

        if commit:
            profile.save()

        return profile
