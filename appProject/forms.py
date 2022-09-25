from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import product_sneakers, product_t_shirt, product_hat, product_pant, product_football_sneakers

# Register user
class register_user_form(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'style':'margin-bottom: 25px'}))
    first_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control', 'style':'margin-bottom: 25px'}))
    last_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control', 'style':'margin-bottom: 25px'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(register_user_form, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


# Update user
class update_user_form(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'style':'margin-bottom: 15px'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style':'margin-bottom: 15px'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style':'margin-bottom: 15px'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style':'margin-bottom: 15px'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


# Change password
class change_password_form(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'style':'margin-bottom: 15px'}))
    new_password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'style':'margin-bottom: 15px'}))
    new_password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'style':'margin-bottom: 15px'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

# Add product
class add_sneakers_form(forms.ModelForm):
    class Meta:
        model = product_sneakers
        fields = ('product_name', 'product_description', 'product_price', 'product_image')

        labels = {
            'product_name': 'Enter you product name',
            'product_description': 'Enter you product description',
            'product_price': 'Enter you product price',
            'product_image': 'Enter you product image',
        }
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-name', 'style':'margin-bottom: 30px', 'id':'product_name'}),
            'product_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-description', 'style':'margin-bottom: 30px', 'id':'product_description'}),
            'product_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-price', 'style':'margin-bottom: 30px', 'id':'product_price'}),
        }

class add_t_shirts_form(forms.ModelForm):
    class Meta:
        model = product_t_shirt
        fields = ('product_name', 'product_description', 'product_price', 'product_image')

        labels = {
            'product_name': 'Enter you product name',
            'product_description': 'Enter you product description',
            'product_price': 'Enter you product price',
            'product_image': 'Enter you product image',
        }
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-name', 'style':'margin-bottom: 30px', 'id':'product_name'}),
            'product_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-description', 'style':'margin-bottom: 30px', 'id':'product_description'}),
            'product_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-price', 'style':'margin-bottom: 30px', 'id':'product_price'}),
        }

class add_hats_form(forms.ModelForm):
    class Meta:
        model = product_hat
        fields = ('product_name', 'product_description', 'product_price', 'product_image')

        labels = {
            'product_name': 'Enter you product name',
            'product_description': 'Enter you product description',
            'product_price': 'Enter you product price',
            'product_image': 'Enter you product image',
        }
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-name', 'style':'margin-bottom: 30px', 'id':'product_name'}),
            'product_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-description', 'style':'margin-bottom: 30px', 'id':'product_description'}),
            'product_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-price', 'style':'margin-bottom: 30px', 'id':'product_price'}),
        }

class add_pants_form(forms.ModelForm):
    class Meta:
        model = product_pant
        fields = ('product_name', 'product_description', 'product_price', 'product_image')

        labels = {
            'product_name': 'Enter you product name',
            'product_description': 'Enter you product description',
            'product_price': 'Enter you product price',
            'product_image': 'Enter you product image',
        }
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-name', 'style':'margin-bottom: 30px', 'id':'product_name'}),
            'product_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-description', 'style':'margin-bottom: 30px', 'id':'product_description'}),
            'product_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-price', 'style':'margin-bottom: 30px', 'id':'product_price'}),
        }

class add_football_sneakers_form(forms.ModelForm):
    class Meta:
        model = product_football_sneakers
        fields = ('product_name', 'product_description', 'product_price', 'product_image')

        labels = {
            'product_name': 'Enter you product name',
            'product_description': 'Enter you product description',
            'product_price': 'Enter you product price',
            'product_image': 'Enter you product image',
        }
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-name', 'style':'margin-bottom: 30px', 'id':'product_name'}),
            'product_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-description', 'style':'margin-bottom: 30px', 'id':'product_description'}),
            'product_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add-price', 'style':'margin-bottom: 30px', 'id':'product_price'}),
        }
