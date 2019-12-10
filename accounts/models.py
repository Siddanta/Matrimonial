from django.db import models
from django.db.models.signals import post_save,pre_save
from django.urls import reverse
from django.conf import settings
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from datetime import date,time
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .utilities import unique_slug_generator
#measurement of height, weight
from django_measurement.models import MeasurementField
from measurement.measures import Weight, Distance
#modeladmin
from django.contrib.admin import ModelAdmin
from django.contrib import admin


from django.utils import timezone
User = settings.AUTH_USER_MODEL
from datetime import datetime, timedelta, date
class ModelManager(models.Manager):
    def update_all(self):
        queryset = self.all()
        now = timezone.now()
        offset = now - datetime.timedelta(hours=12)
        offset2 = now - datetime.timedelta(hours=36)
        queryset.filter(updated__gt=offset2).filter(updated__lte=offset)
        a = 0
        if queryset.count() > a:
            for i in queryset:
                i.check_update()

class UserProfileModel(models.Model):
    #this site details
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True)
    slug = models.CharField(max_length=60,default="asdfasdf")
    Email = models.EmailField(default='@')
    Password = models.CharField(max_length=18, default='pass')
    mark_as_read = models.BooleanField(default=False)

    first_login = models.BooleanField(default=False)

    #personal info
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    DOB = models.DateField(default=datetime.now)
    YourWeight = MeasurementField(measurement=Weight, unit_choices= (('kg','kg'),('kg','kg')),blank=True, null=True)
    YourHeight = MeasurementField(measurement=Distance,unit_choices=(('ft','ft'),('ft','ft')),blank=True, null=True)
    Gender_choices =(
         ('Male', 'Male'),
         ('Female', 'Female'),
         ('Other','Other')
    )

    Gender = models.CharField(max_length=20, choices=Gender_choices)
    Religion_choices = (
        ('Hindu', 'Hindu'),
        ('Muslim', 'Muslim'),
        ('Christian', 'Christian'),
        ('Buddhist', 'Buddhist'),
        ('other', 'other'),

    )
    residency_choices=(
        ('Citizen','Citizen'),
        ('Permanent Resident', 'Permanent Resident'),
        ('Student Visa','Student Visa'),
        ('Temporary Visa','Temporary Visa'),
        ('Work Permit','Work Permit'),
    )
    ResidencyStatus = models.CharField(max_length=20,choices=residency_choices, default=0)
    Religion = models.CharField(max_length=10, choices=Religion_choices)
    MotherTongue = models.CharField(max_length=20)
    Country = CountryField()

    MaritalStatus_choices = (
        ('Never Married', 'Never Married'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),

        ('Widowed','Widowed'),
        ('Awaiting Divorce','Awaited Divorce'),
        ('Annulled','Annulled'),

    )
    MaritalStatus = models.CharField(max_length=30, choices=MaritalStatus_choices, null=True,blank=True)
    community_choices=(
        ('Brahmin','Brahmin'),
        ('Chhetri','Chhetri'),
        ('Newar','Newar'),
        ('Thakuri','Thakuri'),
        ('Gurung','Gurung'),

    )
    Community = models.CharField(max_length=30, null=True,blank=True, choices=community_choices)

    PhotoFile = models.ImageField('Photo', upload_to='Profile_image')

    level_choices = (
        ('Doctorate','Doctorate'),
        ('Bachelors','Bachelors'),
        ('Diploma','Diploma'),
        ('Masters','Masters'),
        ('UnderGraduate','UnderGraduate'),
        ('High School','High School'),
        ('Less than High School','Less than High School'),
    )
    EducationLevel = models.CharField(max_length=30, null=True,blank=True,choices=level_choices)
    Field_choices = (
        ('Advertising/Marketing', 'Advertising/Marketing'),
        ('Armed Forces', 'Bachelors'),
        ('Arts', 'Arts'),
        ('Travel & Tourism', 'Travel & Tourism'),
        ('Computer/IT', 'Computer/IT'),
        ('Fashion', 'Fashion'),
        ('Medicine', 'Medicine'),
        ('Commerce', 'Commerce'),
        ('Engineering/Technology', 'Engineering/Technology'),
        ('Architecture', 'Architecture'),
        ('Agriculture', 'Agriculture'),
        ('Law', 'Law'),
        ('Law', 'Law'),
        ('Nursing/Health Science', 'Nursing/Health Science'),

    )
    EducationField = models.CharField(max_length=50, choices=Field_choices,null=True,blank=True)
    CollegeYouAttend = models.CharField(max_length=50, blank=True,null=True)

    work_choice = (
        ('Private Company','Private Company'),
        ('Government/ Public Sector','Government/ Public Sector'),
        ('Defence/Civil Services','Defence/Civil Services'),
        ('Business/Self Employee','Business/Self Employee'),
        ('Not Working','Not Working'),


    )
    YouWorkWith = models.CharField(max_length=50, choices=work_choice,blank=True,null=True)
    As = models.CharField(max_length=30, blank=True,null=True)
    YourBusiness = models.CharField(max_length=30, blank=True,null=True)
    yourIncome_choices = (

        ('less 5 lacs','less 5 lacs'),
        ('5 lacs to 10 lacs', '5 lacs to 10 lacs'),
        ('10 lacs to 15 lacs', '10 lacs to 15 lacs'),
        (' 15 lacs to 20 lacs', '15 lacs to 20 lacs'),
        ('20 lacs to 25 lacs', '20 lacs to 25 lacs'),
        ('25 lacs to 30 lacs', '25 lacs to 30 lacs'),
        ('30 lacs to 35 lacs', '30 lacs to 35 lacs'),
        ('35 lacs to 40 lacs', '35 lacs to 40 lacs'),
        ('more than 40 lacs', 'More than 40 lacs'),

    )
    YourAnnualIncome = models.CharField(null=True,blank=True,choices=yourIncome_choices,max_length=30)
    aboutYou = models.CharField(max_length=800, null=True,blank=True)




    #life Style
    smoke_choices =(
        ('yes', 'yes'),
        ('no', 'no'),
        ('Occasionally', 'Occasionally'),

    )

    drink_choices =(
        ('yes','yes'),
        ('no','no'),
        ('Occasionally','Occasionally'),
    )

    diet_choices = (

        ('Veg','Veg'),
        ('Non-Veg','Non-Veg'),
        ('Occasionally Non-Veg','Ocassionally Non-Veg'),
        ('Eggetarian','Eggetarian'),
        ('Veggie','Veggie'),
    )
    diet = models.CharField(max_length=30,choices=diet_choices,null=True,blank=True)
    Smoke = models.CharField(choices=smoke_choices, null=True,blank=True, max_length=20)
    Drink = models.CharField(choices=drink_choices, null=True,blank=True, max_length=20)



    body_choices=(
        ('Slim', 'Slim'),
        ('Athletic', 'Athletic'),
        ('Average', 'Average'),
        ('Heavy', 'Heavy'),
    )
    BodyType = models.CharField(max_length=30,blank=True,choices=body_choices,null=True)
    skin_choices = (
        ('Very Fair', 'Very Fair'),
        ('Fair', 'Fair'),
        ('Tan', 'Tan'),
        ('Dark','Dark'),
    )
    SkinTOne=models.CharField(max_length=30,null=True,blank=True,choices=skin_choices)
    MobileNo=PhoneNumberField(null=True,blank=True)

    #family field
    FatherStatus_choices = (
        ('Employed','Employed'),
        ('Business','Business'),
        ('Retired','Retired'),
        ('Not Employed','Not Employed'),
        ('Passed Away','Passed Away'),
    )
    FatherStatus=models.CharField(max_length=30,null=True,blank=True,choices=FatherStatus_choices)
    MotherStatus_choices = (
        ('Home Maker', 'Home Maker'),
        ('Business', 'Business'),
        ('Retired', 'Retired'),
        ('Not Employed', 'Not Employed'),
        ('Passed Away', 'Passed Away'),
    )
    MotherStatus=models.CharField(max_length=30,null=True,blank=True,choices=MotherStatus_choices)
    NoOfBrother=models.PositiveIntegerField(default=None,null=True)
    NoOfSister=models.PositiveIntegerField(default=None,null=True)

    Affluence_choices=(
        ('Affluent','Affluent'),
        ('Middle Class','Middle Class'),
        ('Lower Middle Class','Lower Middle Class'),
        ('Upper Middle Class','Upper Middle Class'),
    )
    FamilyAffluence=models.CharField(max_length=30,choices=Affluence_choices,null=True,blank=True)
    Values_choices = (
        ('Traditional', 'Traditional'),
        ('Moderate', 'Moderate'),
        ('Liberal', 'Liberal'),
    )
    FamilyValues=models.CharField(max_length=30,choices=Values_choices,null=True,blank=True)

    # disable
    disable_choices=(
        ('yes','yes'),
        ('no', 'no'),

    )

    AnyDisability=models.CharField(max_length=30, choices=disable_choices, null=True,blank=True)
    # time
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    age = models.PositiveIntegerField(default=0)

    objects = ModelManager()

    def __str__(self):
        return str(self.user)

    def check_update(self):
        now = timezone.now()
        offset = now - datetime.timedelta(hour=12) # 12 hrs go
        if self.updated <= offset:
            self.do_match()
        else:
            print('already_updated')

    def get_absolute_url(self):
       # return f"/product/{self.title}/"
        return reverse('main_product:detail', kwargs={'my_slug': self.user.id})

    def like_link(self):
        url = reverse('likes:like_user', kwargs={'id': self.user.id})
        return url




    @property
    def get_age(self):
        d = datetime.combine(self.DOB,datetime.min.time())
        return (datetime.today() - d).days / 365.25
        # dob = self.DOB
        # tod = date.today()
        # my_age = (tod.year - dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))
        # return my_age

    def save(self, *args, **kwarg):
        self.age = self.get_age
        super(UserProfileModel, self).save(*args, **kwarg)

# def calc_age(D_O_B):
#
#     D_O_B = str(D_O_B)
#     res = datetime.strptime(D_O_B)
#     age = int((date.today - res).days / 365.25)
#     return age


# @receiver(pre_save,sender=UserProfileModel)
# def update_age(sender,instance,*args,**kwargs):
#     age = calc_age(instance.DOB)
#     instance.age = age















# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfileModel.objects.create(user=kwargs['instance'])
#         user_profile.save()
#
# post_save.connect(create_profile, sender=User)


# @receiver(pre_save, sender=UserProfileModel) # decoraters
# def pre_save_slug(sender,**kwargs):
#     print(kwargs)
#     slug = unique_slug_generator(kwargs["instance"])
#     #slug = slugify(kwargs["instance"].title)
#     kwargs["instance"].slug = slug


