from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u'username',
        error_messages={'required': 'please input the username'}
    )
    password = forms.CharField(
        required=True,
        label=u'password',
        error_messages={'required': 'please input the passwordF'}
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u'username and password are required')
        else:
            cleaned_data = super(LoginForm, self).clean();
