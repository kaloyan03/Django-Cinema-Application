from django import forms
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm, PasswordResetForm, \
    SetPasswordForm
from django.core.exceptions import ValidationError
from django.template.defaultfilters import capfirst
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    """
       A form that creates a user, with email and password.
       """

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }

    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'input-field',
                'placeholder': 'E-mail',
            }
        )
    )

    password1 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "input-field",
                'placeholder': 'Password',
            }
        ),
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "input-field",
                'placeholder': 'Confirm password',
            }
        ),
        strip=False,
    )

    class Meta:
        model = UserModel
        fields = ("email", "password1", "password2")
        field_classes = {"email": UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SignInForm(AuthenticationForm):
    username = UsernameField(
        label='',
        required=True,
        widget=forms.EmailInput(attrs={"autofocus": True, "class": "input-field", "placeholder": "Email"})
    )
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "input-field", "placeholder": "Password"}),
    )


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = ""
        self.fields['email'].widget = forms.EmailInput(attrs={"placeholder": "E-mail", 'class': 'input-field'})


class PasswordSetForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].label = ""
        self.fields['new_password2'].label = ""
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={"placeholder": "Password", 'class': 'input-field'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={"placeholder": "Repeat password", 'class': 'input-field'})
