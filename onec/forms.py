from django import forms


class SignInForm(forms.Form):
    user_name = forms.CharField(label="Login", widget=forms.TextInput(attrs={'class': 'form-control open-sans-500', 'id': 'username'}))
    user_email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control open-sans-500', 'id': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control open-sans-500', 'id': 'psw'}), label="Password")
    password_conf = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control open-sans-500', 'id': 'psw_c'}),
                                    label="Confirm password")