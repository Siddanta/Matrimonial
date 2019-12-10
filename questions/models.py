from django.db import models

# Create your models here.
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.urls import reverse
#for signals
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

class Question(models.Model):
    text= models.TextField(blank=True,null=True)
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    #answer = models.ManyToManyField('Answer')
    def __str__(self):
        return self.text




class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,null=True, blank=True)
    text = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.text
    # def get_absolute_url(self):
    #    # return f"/product/{self.title}/"
    #     return reverse('main-product:question_single', kwargs={'id': self.user.id})


Level_choices= (('Mandatory','Mandatory'),
                ('Very Important','Very Important'),
                ('Somewhat  Important','Somewhat Important'),
                ('Not Important','Not Important'),

                )



class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    my_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True, related_name='user_answer')
    my_answer_importance = models.CharField(max_length=50,choices=Level_choices,null=True, blank=True)
    my_points = models.IntegerField(default=-1)
    their_answer = models.ForeignKey(Answer, on_delete=models.CASCADE,null=True, blank=True,related_name='match_answer')
    their_importance = models.CharField(max_length=50, choices=Level_choices,null=True,blank=True)
    their_points = models.IntegerField(default=-1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.question.text[:30])



def score_points(importance_level):
    if importance_level =='Mandatory':
        points=300
    elif importance_level =='Very Important':
        points=200
    elif importance_level == 'Somewhat  Important':
        points=50
    elif importance_level == 'Not Important':
        points=0
    else:
        points=0
    return points


@receiver(pre_save,sender=UserAnswer)# save as line no 64 i.e pre_save()
def update_user_answer_score(sender,instance,*args,**kwargs):
    my_points = score_points(instance.my_answer_importance)
    instance.my_points = my_points
    their_points = score_points(instance.their_importance)
    instance.their_points = their_points


# pre_save.connect(update_user_answer_score,sender=UserAnswer)
# def update_user_answer_score(sender,instance,created,*args,**kwargs):
#     print(sender)
#     print(instance)
#     print(created)
#     if created:
#         if instance.my_points == -1:
#             my_points = score_points(instance.my_answer_importance)
#             instance.my_points = my_points
#             instance.save()
#
# post_save.connect(update_user_answer_score,sender=UserAnswer)


class QuestionAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question1 = models.TextField(default='what Family affluence you prefer?',null=True,blank=True)
    answer1_choices = (
        ('Affluent','Affluent'),
        ('Middle Class','Middle Class'),
        ('Lower Middle Class','Lower Middle Class'),
        ('Upper Middle Class','Upper Middle Class'),
    )
    Answer1 = models.CharField(max_length=20,choices=answer1_choices,null=True,blank=True)
    question2 = models.TextField(default='what Family values you prefer?',null=True,blank=True)
    answer2_choices = (
        ('Traditional', 'Traditional'),
        ('Moderate', 'Moderate'),
        ('Liberal', 'Liberal'),
    )
    Answer2 = models.CharField(max_length=20,choices=answer2_choices,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.user)
