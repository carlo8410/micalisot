from django import forms

class UsuarioForm(forms.Form):
    u_nombre = forms.CharField(max_length= 200,required=True,
                               widget=forms.TextInput(attrs= {'class': "form-control"}),
                              )