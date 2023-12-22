from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import SafeString
from django.utils.translation import gettext_lazy as _

from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, label='', widget=forms.TextInput())
    password = forms.CharField(max_length=65, label='', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = ''
        self.fields["username"].help_text = None
        self.fields["username"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username...'})

        self.fields["password"].label = ''
        self.fields["password"].help_text = None
        self.fields["password"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password...'})


class RegisterForm(UserCreationForm):
    error_messages = {
        "unique": _("Bunday foydalanuvchi nomiga ega foydalanuvchi allaqachon mavjud.")
    }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = ''
        self.fields["username"].help_text = None
        self.fields["username"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username...'})

        self.fields["first_name"].label = ''
        self.fields["first_name"].help_text = None
        self.fields["first_name"].widget.attrs.update({'class': 'form-control', 'placeholder': 'First name...'})

        self.fields["last_name"].label = ''
        self.fields["last_name"].help_text = None
        self.fields["last_name"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last name...'})

        self.fields["password1"].label = ''
        self.fields["password1"].help_text = None
        self.fields["password1"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password..'})

        self.fields["password2"].label = ''
        self.fields["password2"].help_text = None
        self.fields["password2"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password confirm...'})

        self.fields["email"].label = ''
        self.fields["email"].help_text = None
        self.fields["email"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email...'})

        # self.error_messages = {
        #     'required': 'Пароли не совпадают.',
        #     # Другие общие сообщения об ошибках
        # }

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        # help_texts = {
        #     "username": "TI OBYAZN!!! 150 yoki undan kam belgi. Faqat harflar, raqamlar va @/./+/-/_"
        # }
