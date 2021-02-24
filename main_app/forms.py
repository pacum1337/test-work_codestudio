from django import forms


class SendMailForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'text-box',
        'placeholder': 'Ваше имя',
        'onfocus': 'blurEvent(this)',
        'onkeyup': 'onChangeEvent(this)',
        'id': 'name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'text-box',
        'placeholder': 'Электронная почта',
        'onfocus': 'blurEvent(this)',
        'onkeyup': 'onChangeEvent(this)',
        'id': 'email'
    }))
