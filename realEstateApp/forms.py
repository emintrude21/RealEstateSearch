from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import AuthUser, Comment, Agent
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Homesforsale

class signupform(forms.ModelForm):
    password1 = forms.CharField(label = 'Password1', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'password2', widget = forms.PasswordInput)

    class Meta:
        model = AuthUser
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_superuser'].initial = 0
        self.fields['is_superuser'].widget = forms.HiddenInput()
        self.fields['is_staff'].initial = 0
        self.fields['is_staff'].widget = forms.HiddenInput()
        self.fields['is_active'].initial = 1
        self.fields['is_active'].widget = forms.HiddenInput()
        self.fields['last_login'].widget = forms.HiddenInput()

        if not self.instance.pk:
            self.initial['date_joined'] = timezone.now()

        self.fields['date_joined'].widget = forms.HiddenInput()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if AuthUser.objects.filter(username = username).exists():
            raise forms.ValidationError('Username is already taken. Please choose a different one.')
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Passwords do not match")
        
        return cleaned_data
    
    def save(self, commit = True):
        user = super().save(commit = False)
        user.password = make_password(self.cleaned_data["password1"])
        user.last_login = timezone.now()
        if commit:
            user.save()
        return user
    
class salesdata(forms.Form):
    beds = forms.IntegerField(required = False)
    bathrooms = forms.IntegerField(required = False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
    
class agentsignupform(forms.ModelForm):
    password1 = forms.CharField(label = 'password1', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'password2', widget = forms.PasswordInput)

    class Meta:
        model = AuthUser
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_superuser'].initial = 0
        self.fields['is_superuser'].widget = forms.HiddenInput()
        self.fields['is_staff'].initial = 1
        self.fields['is_staff'].widget = forms.HiddenInput()
        self.fields['is_active'].initial = 1
        self.fields['is_active'].widget = forms.HiddenInput()
        self.fields['last_login'].widget = forms.HiddenInput()

        if not self.instance.pk:
            self.initial['date_joined'] = timezone.now()

        self.fields['date_joined'].widget = forms.HiddenInput()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if AuthUser.objects.filter(username = username).exists():
            raise forms.ValidationError('Username is already taken. Please choose a different one.')
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Passwords do not match")
        
        return cleaned_data
    
    def save(self, commit = True):
        user = super().save(commit = False)
        user.password = make_password(self.cleaned_data["password1"])
        user.last_login = timezone.now()
        if commit:
            user.save()
        return user
    
class AgentForm(forms.ModelForm): 
    class Meta:
        model = Agent
        fields = ['state', 'city', 'agent_name', 'agency', 'specialities', 'about_me',
                  'broker_address', 'cellphone', 'brokerphone', 'screenname', 'licenses', 
                  'other_licenses', 'language1', 'language2']

class SalesForm(forms.ModelForm):
    class Meta:
        model = Homesforsale
        fields = ['status_type', 'status_text', 'price', 'area', 'price_per_sqft', 'lot_area', 
                  'lot_area_unit', 'beds', 'bathrooms', 'address', 'street', 'city', 'state', 
                  'zipcode', 'latitude', 'longitude', 'broker_name', 'image_url', 'description', 
                  'built_in', 'est_pay', 'residence_type' , 'full_bathroom', 'half_bathroom', 'basement', 
                  'flooring', 'heating', 'cooling', 'appliances', 'interior_features', 'parking', 'property', 
                  'lot', 'construction_type', 'material', 'utility', 'community', 'location', 'agency_fee', 'agent_email']

class AddNewListing(forms.ModelForm):
    add_new_listing = forms.BooleanField(label='Add New Listing', required=False)
    class Meta:
        model = Homesforsale
        fields = ['status_type', 'status_text', 'price', 'area', 'price_per_sqft', 'lot_area', 
                  'lot_area_unit', 'beds', 'bathrooms', 'address', 'street', 'city', 'state', 
                  'zipcode', 'latitude', 'longitude', 'broker_name', 'image_url', 'description', 
                  'built_in', 'est_pay', 'residence_type' , 'full_bathroom', 'half_bathroom', 'basement', 
                  'flooring', 'heating', 'cooling', 'appliances', 'interior_features', 'parking', 'property', 
                  'lot', 'construction_type', 'material', 'utility', 'community', 'location', 'agency_fee', 'agent_email']

class InquiryForm(forms.Form):
    name = forms.CharField(max_length = 100)
    message = forms.CharField(widget = forms.Textarea)