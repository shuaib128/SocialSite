from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#UserRegester form
class UserRegesterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
        
    #checking if email existis in database
    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError("This Email Already Used. Please Check Again")
        return email

    #saving info in database
    def save(self, commit=True):
        user = super(UserRegesterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user




#User Info update form

#User Profile Pic
class UsePicUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['images']

#User info Update
class UseUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']


#user profileinfo update
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['coverPhoto', 'biodata', 'birthday']

#user contact update
class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile', 'website', 'facebook', 'twitter']

        