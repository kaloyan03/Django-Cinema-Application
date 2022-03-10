from django import forms
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.template.defaultfilters import capfirst
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    """
       A form that creates a user, with no privileges, from the given username and
       password.
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
    email = UsernameField(
        label='',
        widget=forms.TextInput(attrs={"autofocus": True, "class": "input-field"})
    )
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "input-field"}),
    )

    class Meta:
        model = UserModel
        fields = ('email', 'password',)
        field_classes = {"email": UsernameField}