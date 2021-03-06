from django import forms

class ContactFom(forms.Form):
    fullname = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your full name"
                }
                )
        )
    email    = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                "class": "form-control",
                "placeholder": "Your email"
                }
                )
        )
    content  = forms.CharField(
            widget=forms.Textarea(
                attrs={
                "class": "form-control",
                "placeholder": "Your message"
                }
                )
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
