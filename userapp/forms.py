from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from .models import *

# SIGNUP FORM


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("First_name", "Last_name", "User_name",
                  "Email", "College_name", "Department",
                  "Year_of_admission", "Year_of_graduation",
                  "Account_verification")
        # "__all__"
        widgets = {
            'First_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'User_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'College_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Department': forms.TextInput(attrs={'class': 'form-control'}),
            'Year_of_admission': forms.TextInput(attrs={'class': 'form-control'}),
            'Year_of_graduation': forms.TextInput(attrs={'class': 'form-control'}),
            'Account_verification': forms.TextInput(attrs={'class': 'form-control'}),
            'Account_suspension_status': forms.TextInput(attrs={'class': 'form-control'}),
            'User_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'User_ID': forms.TextInput(attrs={'class': 'form-control'}),

        }


# LOGIN FORM
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ("Email", "Password")
        widgets = {
            # 'User_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', "placeholder": "JohnDoe@gmail.com"}),
            'Password': forms.TextInput(attrs={'class': 'form-control', "placeholder": "*********"})

        }
        # "__all__"


# VALIDATE FORM
class ValidateForm(forms.ModelForm):
    class Meta:
        model = Validation
        fields = ("School_ID_Front_View", "School_ID_Back_View")
        widgets = {
            # 'Your User Name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "JohnDoe@gmail.com"}),
            'Your Student ID[Front View]': forms.TextInput(attrs={'class': 'form-control'}),
            'Your Student ID[Back View]': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class ValidateForm2(forms.ModelForm):
    class Meta:
        model = Validation2
        fields = "__all__"
        widgets = {
            'School_Email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


# VIDEO UPLOAD FORM
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video_Files
        fields = ("Title", "Video_description",
                  "Video_File", "Video_Visibility")
        widgets = {
            # 'Date_Time': forms.TextInput(attrs={'class': 'form-control'}),
            'Title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter Video Title'}),
            'Video_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Video Description', 'title': ' '}),
            'Video_File': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload Video'}),
            'Video_Visibility': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Public Or Private'})
        }
# COMMENT FORM


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("User_ID", "Comments")
        # "__all__"
        widgets = {
            'Comments_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'Comments': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Enter Your Comment"}),
            'User_ID': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Select Your User ID"}),

        }


# # EMAIL VERIFICATION FORM

# class EmailVerify(forms.ModelForm):
#     email = forms.EmailField(max_length=200, help_text='Required')

#     class Meta:
#         model = Email_setup
#         fields = ('username', 'email', 'password1', 'password2')
