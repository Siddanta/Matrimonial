from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
import decimal
from decimal import Decimal
# Create your models here.

from .utils import get_match



class MatchQuerySet(models.query.QuerySet):
    def all(self):
        return self.filter()

    def matches(self, user):
        q1 = self.filter(user_a=user).exclude(user_b=user)
        q2 = self.filter(user_b=user).exclude(user_a=user)
        return (q1 | q2).distinct()

class MatchManager(models.Manager):
    def get_queryset(self):
        return MatchQuerySet(self.model, using=self._db)

    def get_or_create_match(self, user_a=None, user_b=None):
        try:
            obj = self.get(user_a=user_a, user_b=user_b)
        except:
            obj = None
        try:
            obj_2 = self.get(user_a=user_b, user_b=user_a)
        except:
            obj_2 = None
        if obj and not obj_2:
            obj.check_update()
            return obj, False
        elif not obj and obj_2:
            obj_2.check_update()
            return obj_2, False
        else:
            new_instance = self.create(user_a=user_a, user_b=user_b)
            #add_match


            new_instance.do_match()
            return new_instance, True

    def update_all(self):
        queryset = self.all()
        now = timezone.now()
        offset = now - datetime.timedelta(seconds=12)
        offset2 = now - datetime.timedelta(hours=36)
        queryset.filter(updated__gt=offset2).filter(updated__lte=offset)
        a = 0
        if queryset.count() > a:
            for i in queryset:
                i.check_update()

    def matches_all(self,user):
        return self.get_queryset().matches(user)

class Match(models.Model):

    user_a = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='match_user_a')
    user_b = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='match_user_b')
    match_decimal = models.DecimalField(decimal_places=8,max_digits=16,default=0.0)
    question_answered = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    @property
    def get_percent(self):
        z = self.match_decimal
        b = 100
        c = decimal.Decimal(b)
        a =   decimal.Decimal(z)* decimal.Decimal(c)
        return a

    def __str__(self):
        return str(self.match_decimal)
    objects = MatchManager()

    def do_match(self):
        user_a = self.user_a
        user_b = self.user_b
        match_decimal, questions_answered = get_match(user_a, user_b)
        self.match_decimal = match_decimal
        self.questions_answered = questions_answered
        self.save()

    def check_update(self):
        now = timezone.now()
        offset = now - datetime.timedelta(seconds=12) # 12 hrs go
        if self.updated<= offset:
            self.do_match()
        else:
            print('already_updated')

