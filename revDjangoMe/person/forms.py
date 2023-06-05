from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['cin', 'first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        # user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user