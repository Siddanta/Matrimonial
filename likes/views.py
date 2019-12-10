from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model


from .models import Like
# Create your views here.
User = get_user_model()


def like_user(request, id):
    pending_like = get_object_or_404(User, id=id)
    user_like, created = Like.objects.get_or_create(user=request.user)
    if pending_like in user_like.liked_users.all():
        user_like.liked_users.remove(pending_like)
    else:
        user_like.liked_users.add(pending_like)
    return redirect('accounts:detail', my_username=pending_like.username)