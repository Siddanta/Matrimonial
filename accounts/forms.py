from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import UserProfileModel
from django.forms.utils import  ValidationError
from django.shortcuts import get_object_or_404

class RegistrationForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)



        if commit:
            user.save()
        return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User

        fields = ('username','password')


class ProfileForm(forms.ModelForm):


    class Meta:
        model = UserProfileModel
        labels = {'Fname': 'First Name',
                  'Lname' : 'Last Name'
                  }
        fields = ['Email','Fname','Lname','DOB', 'Gender' ]



class ProfileForm1(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        labels = {'MotherTongue': 'Mother Tongue',
                  'MaritalStatus': 'Marital Status',
                  }
        fields = ['Religion', 'Country', 'MotherTongue','MaritalStatus','Community']


class ProfileForm2(forms.ModelForm):
    class Meta:
        model =UserProfileModel
        labels = {
            'EducationLevel':'Education Level',
            'EducationField':'Education Field',
            'CollegeYouAttend':'College You Attend',
            'YouWorkWith':'You Work With',
            'YourBusiness':'Your Business',
            'YourAnnualIncome':'Your Annual Income',
        }
        fields = ['EducationLevel', 'EducationField','CollegeYouAttend','YouWorkWith','As','YourBusiness','YourAnnualIncome']









class ProfileForm3(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        labels = {
            'BodyType':'Body Type',
            'SkinTOne': 'Skin TOne',
            'YourWeight':'Your Weight',
            'YourHeight':'Your Height',
            }
        fields = ['diet','Smoke','Drink','BodyType','SkinTOne','YourWeight','YourHeight']


class ProfileForm4(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        labels={
            'MobileNo': 'Mobile Number',
            'NoOfBrother':'No Of Brother',
            'NoOfSister':'No Of Sister',
            'FatherStatus': 'Father Status',
            'MotherStatus':'Mother Status',
            'FamilyAffluence':'Family Affluence',
            'FamilyValues':'Family Values',
        }
        fields = ['MobileNo','NoOfBrother','NoOfSister','FatherStatus','MotherStatus','FamilyAffluence','FamilyValues']


class ProfileForm5(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        labels ={'aboutYou':'About You',
                 'PhotoFile':'Upload Photo',
                 'AnyDisability':'Any Disability',
                 }

        fields = ['AnyDisability','PhotoFile','aboutYou']

        widgets = {
            'aboutYou': forms.Textarea(attrs={'rows': 5,'cols': 25}),
        }




