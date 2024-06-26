from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Researcher, Project, Publication


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ResearcherForm(forms.ModelForm):
    class Meta:
        model = Researcher
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'
