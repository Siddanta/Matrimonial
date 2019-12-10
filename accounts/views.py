from django.shortcuts import render, redirect, HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, render_to_response,Http404
from .models import UserProfileModel

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import auth
# for reverse url
from django.urls import reverse
from django.http import JsonResponse
# forms
from .forms import (ProfileForm,
                    RegistrationForm,
                    ProfileForm1,
                    ProfileForm2,
                    ProfileForm3,
                    ProfileForm4,
                    ProfileForm5,
                    EditProfileForm, )

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

# like
from likes.models import Like
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth import login as auth_login
# mail
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



#matchmaking
from matches.models import Match

User = get_user_model()


def login(request):
    return render(request, "accounts/login.html")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()



            return redirect('../../accounts/login')

    else:
        form = RegistrationForm()
    args = {'form': form}

    return render(request, 'accounts/register.html', args)


def edit_username(request):
    if request.method == 'POST':

        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('../../accounts/edit_all')

    else:
        form = EditProfileForm(instance=request.user)
    args = {'form': form}

    return render(request, 'accounts/edit_username.html', args)


def edit_password(request):
    if request.method == 'POST':

        form = PasswordChangeForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('../../accounts/edit_all')

    else:
        form = PasswordChangeForm(user=request.user)
    args = {'form': form}

    return render(request, 'accounts/edit_password.html', args)


@login_required()
def register1(request):
    pro = get_object_or_404(UserProfileModel, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST or None, instance=pro)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.user = request.user
            pro.save()
            # send_mail(subject,messages,from_email,to_list,fail_silently=True)
            subject = 'For Email Confirmation'
            messages = 'Welcome to LaganGAtho.com! Please Confirm your Email'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [pro.Email, settings.EMAIL_HOST_USER]
            send_mail(subject, messages, from_email, recipient_list, fail_silently=False)
            return redirect('/accounts/register2')
    else:
        form = ProfileForm()

    args = {'form': form}
    return render(request, 'accounts/register1.html', args)

@login_required
def edit_register1(request,my_id):
    user = UserProfileModel.objects.get(user=request.user)
    my_record = UserProfileModel.objects.get(id=my_id)
    if request.method == 'POST':

        form = ProfileForm(request.POST, instance=my_record)
        if form.is_valid():
            form.save()
            return redirect('accounts:edit_register2', my_id)

    else:
        form = ProfileForm(instance=my_record)
        args = {'form': form,
                'user':user,
                'my_record': my_record}

    return render(request, 'accounts/edit_register1.html', args)


@login_required
def register2(request):
    pro = get_object_or_404(UserProfileModel, user=request.user)
    if request.method == 'POST':
        form = ProfileForm1(request.POST or None, instance=pro)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.user = request.user
            pro.save()
            return redirect('/accounts/register3')
    else:
        form = ProfileForm1()

    args = {'form': form}
    return render(request, 'accounts/register2.html', args)

@login_required
def edit_register2(request,my_id):
    my_record = UserProfileModel.objects.get(id=my_id)
    if request.method == 'POST':

        form = ProfileForm1(request.POST, instance=my_record)
        if form.is_valid():
            form.save()
            return redirect('accounts:edit_register3', my_id)

    else:
        form = ProfileForm1(instance=my_record)
        args = {'form': form,
                ' my_record': my_record}

    return render(request, 'accounts/edit_register2.html', args)
@login_required
def register3(request):
    pro = get_object_or_404(UserProfileModel, user=request.user)
    if request.method == 'POST':
        form = ProfileForm2(request.POST or None, instance=pro)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.user = request.user
            pro.save()
            return redirect('/accounts/register4')
    else:
        form = ProfileForm2()

    args = {'form': form}

    return render(request, 'accounts/register3.html', args)

@login_required
def edit_register3(request,my_id):
    my_record = UserProfileModel.objects.get(id=my_id)
    if request.method == 'POST':

        form = ProfileForm2(request.POST, instance=my_record)
        if form.is_valid():
            form.save()
            return redirect('accounts:edit_register4', my_id)

    else:
        form = ProfileForm2(instance=my_record)
        args = {'form': form,
                ' my_record': my_record}

    return render(request, 'accounts/edit_register3.html', args)
@login_required
def register4(request):
    pro = get_object_or_404(UserProfileModel, user=request.user)
    if request.method == 'POST':
        form = ProfileForm3(request.POST or None, request.FILES, instance=pro)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.user = request.user
            pro.save()
            return redirect('/accounts/register5')
    else:
        form = ProfileForm3()

    args = {'form': form}
    return render(request, 'accounts/register4.html', args)

@login_required
def edit_register4(request,my_id):
    my_record = UserProfileModel.objects.get(id=my_id)
    if request.method == 'POST':

        form = ProfileForm3(request.POST, instance=my_record)
        if form.is_valid():
            form.save()
            return redirect('accounts:edit_register5', my_id)

    else:
        form = ProfileForm3(instance=my_record)
        args = {'form': form,
                ' my_record': my_record}

    return render(request, 'accounts/edit_register4.html', args)


@login_required
def register5(request):
    pro = get_object_or_404(UserProfileModel, user=request.user)
    if request.method == 'POST':
        form = ProfileForm4(request.POST or None, request.FILES, instance=pro)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.user = request.user
            pro.save()
            return redirect('/accounts/register6')
    else:
        form = ProfileForm4()

    args = {'form': form}
    return render(request, 'accounts/register5.html', args)


@login_required
def edit_register5(request,my_id):
    my_record = UserProfileModel.objects.get(id=my_id)
    if request.method == 'POST':

        form = ProfileForm4(request.POST, instance=my_record)
        if form.is_valid():
            form.save()
            return redirect('accounts:edit_register6', my_id)

    else:
        form = ProfileForm4(instance=my_record)
        args = {'form': form,
                ' my_record': my_record}

    return render(request, 'accounts/edit_register5.html', args)

@login_required
def register6(request):
    pro = get_object_or_404(UserProfileModel, user=request.user)
    if request.method == 'POST':
        form = ProfileForm5(request.POST or None, request.FILES, instance=pro)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.user = request.user
            pro.save()
            return redirect('../afterLogin')
    else:
        form = ProfileForm5()

    args = {'form': form}
    return render(request, 'accounts/register6.html', args)


@login_required
def edit_register6(request,my_id):
    my_record = UserProfileModel.objects.get(id=my_id)
    if request.method == 'POST':

        form = ProfileForm5(request.POST, instance=my_record)
        if form.is_valid():
            form.save()
            return redirect('../../edit_all')

    else:
        form = ProfileForm5(instance=my_record)
        args = {'form': form,
                ' my_record': my_record}

    return render(request, 'accounts/edit_register6.html', args)


import decimal
@login_required()
def after_login(request):

    user = Like.objects.all()
    user_profile, created = UserProfileModel.objects.get_or_create(user=request.user)
    mutual_likes = Like.objects.get_all_mutual_likes(request.user, 4)
    a = Like.objects.check_list(request.user)

    messages.success(request,'you are liked')
    print (messages)





    # print(user[0].user.liked_users)
    # for i in user[0].liked_users:
    #     if self_user == i:
    #         print('Yes')
    #     else:
    #         print('No')
    # print(avc.liked_users)

    # if  ac in avc.liked_users:
    #         print('YES')
    # else:
    #         print ('NO')

    if request.user.is_authenticated:
        match_set = Match.objects.matches_all(request.user).order_by('-match_decimal')
        matches =[]
        for match in match_set:
            if match.get_percent > decimal.Decimal(10) :
                if match.user_a == request.user and match.user_b !=request.user:
                    items_wanted = [match.user_b, match.get_percent]
                    matches.append(items_wanted)
                elif match.user_b == request.user and match.user_a !=request.user:
                    items_wanted = [match.user_a, match.get_percent]
                    matches.append(items_wanted)
                else:
                    pass


        if user_profile.first_login == False:

            pro = get_object_or_404(UserProfileModel, user=request.user)
            if request.method == 'POST':
                form = ProfileForm(request.POST or None, instance=pro)
                if form.is_valid():
                    pro = form.save(commit=False)
                    pro.user = request.user

                    pro.save()
                    user_profile.first_login = True
                    user_profile.save()
                    return redirect('/accounts/register1')
            else:

                form = ProfileForm()

            args = {'form': form}

            return render(request, 'accounts/register1.html', args)


        else:

            mutual_likes = Like.objects.get_all_mutual_likes(request.user, 4)

            if user_profile.Gender == 'Male':

                object = UserProfileModel.objects.filter(Gender='Female')

                context = {
                        "object": object,
                        'matches': matches,
                        'mutual_likes': mutual_likes,
                        'message': messages,
                        'a':a,



                    }

                print(object)
                return render(request, "accounts/home.html", context)
            else:
                object = UserProfileModel.objects.filter(Gender='Male')
                paginator = Paginator(object, 4)
                page = request.GET.get('page')
                try:
                    object = paginator.page(page)
                except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                    object = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    object = paginator.page(paginator.num_pages)
                context = {
                        "object": object,
                        'matches': matches,
                         'mutual_likes':mutual_likes,
                        'message': messages,
                        'a': a,




                    }
                print(object)

                return render(request, "accounts/home.html", context)


# own details


def profile_detail(request, *args, **kwargs):
    user_profile = UserProfileModel.objects.get(user=request.user)
    context = {'user_profile': user_profile}
    return render(request, "accounts/userprofilemodel_owndetail.html", context)


def logout(request):
    auth.logout(request)
    return render(request, '')


# users details
#@login_required
def profile_details(request, my_username):
    # user_profile = UserProfileModel.objects.get(User, slug=my_username)

    # user = get_object_or_404(User, username=my_username)
    if request.user.is_authenticated:
        user = User.objects.get(username=my_username)
        user_profile, creates = UserProfileModel.objects.get_or_create(user=user)

        if user_profile.Smoke == 'no':
            smoke = " Doesn't Smoke"
        else:
            smoke = 'Does Smoke'

        if user_profile.Drink == 'no':
            drink = " Doesn't Drink"
        else:
            drink = 'Does Drink'
        user1 = UserProfileModel.objects.get(user=request.user)
        user2 = UserProfileModel.objects.get(user__username=my_username)



        if user1.Gender != user2.Gender:
            match, created = Match.objects.get_or_create_match(user_a=request.user, user_b=user)

            # print(created)
        else:
            raise Http404
        user_like, user_like_created = Like.objects.get_or_create(user=request.user)

        print(user_like)


        mutual_like = user_like.get_mutual_like(user)
        print(mutual_like)
        do_i_like = False
        if user in user_like.liked_users.all():
            do_i_like = True


        # print (user_like)
        # print (mutual_like)

        context = {'user': 'user',
                   'match': match,
                   'user_profile': user_profile,
                   'mutual_like': mutual_like,
                   'do_i_like': do_i_like,
                   'smoke':smoke,
                   'drink':drink
                   }

        return render(request, "accounts/userprofilemodel_detail.html", context)
    else:
        raise Http404




def edit_prof(request):
    user = UserProfileModel.objects.get(user=request.user)
    return render(request, "accounts/edit_all.html", {'user':user})


def age(request):
    instance = get_object_or_404(UserProfileModel, id=id)

    def calculate():
        import datetime
        return int((datetime.date.today() - instance.DOB).days / 365.25)

    instance.age = calculate()
    context = {"instance": instance}
    return render(request, "search.html", context)


@login_required
def search(request):
    user = UserProfileModel.objects.get(user=request.user)
    if user.Gender == 'Male':

        queryset_list = UserProfileModel.objects.filter(Gender='Female').order_by('-timestamp')
    else:
        queryset_list = UserProfileModel.objects.filter(Gender='Male').order_by('-timestamp')

    # query1 = request.GET.get('Gender')
    query2 = request.GET.get('Community')
    query3 = request.GET.get('Religion')
    query4 = request.GET.get('MaritalStatus')
    query5 = request.GET.get('Country')
    # query6 = request.GET.get('min_age')
    # query7 = request.GET.get('max_age')
    # query7 = request.GET.get('max_age')


    # print(query1)
    print(query2)
    print(query3)
    print(query4)
    print(query5)
    # print(query6)
    # print(query7)


    if query2 and query3 and query4 and query5 :
        # and query2 and query3 and query4 and query5 and query6 and query7:
        # queryset_list = queryset_list.filter(Gender__icontains=query1)
        queryset_list = queryset_list.filter(Community__icontains=query2)
        queryset_list = queryset_list.filter(Religion__icontains=query3)
        queryset_list = queryset_list.filter(MaritalStatus__icontains=query4)
        queryset_list = queryset_list.filter(Country__icontains=query5)
        # queryset_list = queryset_list.filter(age__lte=query6)
        # queryset_list = queryset_list.filter(age__gte=query7)

    paginator = Paginator(queryset_list, 6)  # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        queryset1 = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset1 = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset1 = paginator.page(paginator.num_pages)

    context = {'queryset1': queryset1}

    print(queryset1)
    return render(request, "accounts/search.html", context)
