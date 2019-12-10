from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save

from django.contrib import messages
User = settings.AUTH_USER_MODEL


class UserLikeManager(models.Manager):

    def check_list(self,user):
        users = Like.objects.all()

        for all_user in users:
            liked = all_user.liked_users.all()
            # print(liked)
            for all_liked in liked:
                # print(all_liked)

                if user == all_liked:
                   return all_user






    def get_all_mutual_likes(self, user, number):

        try:
            qs = user.liker.liked_users.all()

        except:
            return None
        mutual_users = [][:number]
        for other_user in qs:
            try:
                if other_user.liker.get_mutual_like(user):
                    mutual_users.append(other_user)
            except:
                pass
        return mutual_users



class Like(models.Model):
    user = models.OneToOneField(User, related_name='liker', on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(User,related_name='liked_users',blank=True)
    objects = UserLikeManager()

    def __str__(self):
        return self.user.username




    def get_mutual_like(self, user_b):
        i_like = False
        you_like = False
        if user_b in self.liked_users.all():
            i_like = True
        liked_user, created = Like.objects.get_or_create(user=user_b)
        if self.user in liked_user.liked_users.all():
            you_like = True
        if you_like and i_like:
            return True
        else:
            return False


    def get_absolute_url(self):
       # return f"/product/{self.title}/"
        return reverse('likes:like_user', kwargs={'id': self.id})



