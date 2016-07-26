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


class AddColumnForm(forms.Form):
    name = forms.CharField(required=True)


class RenameColumnForm(forms.Form):
    columnId = forms.IntegerField(required=True)
    newName = forms.CharField(max_length=20, required=True)


class DeleteColumnForm(forms.Form):
    columnId = forms.IntegerField(required=True)


class DeleteBlogForm(forms.Form):
    blogId = forms.IntegerField(required=True)
