from django.form import Form

class NameForm(Form):
    account = forms.CharField(label='Account Name', max_length=100)
