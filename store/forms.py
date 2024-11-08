from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from store.models import UserProfile,Project


class SignUpForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2"]

        widgets={

            "username":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "email":forms.EmailInput(attrs={"class":"form-control mb-3"}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs["class"] = "form-control mb-3"
        self.fields["password2"].widget.attrs["class"] = "form-control mb-3"

class SignInForm(forms.Form):

    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    password=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))

class UserProfileForm(forms.ModelForm):

    class Meta:

        model=UserProfile

        fields=["bio","profile_picture","phone"]

class ProjectForm(forms.ModelForm):

    class Meta:

        model=Project

        fields=["title","description",
                "preview_image","price",
                "files","tag_objects",
                "thumbnail"
                ]

class PasswordResetForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control mb-3"}))

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-4"}))

       