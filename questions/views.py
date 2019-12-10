from django.shortcuts import render, redirect, Http404

from django.shortcuts import get_object_or_404, render_to_response
#for login required
from django.contrib.auth.decorators import login_required
#from own files
from .models import QuestionAnswer,Question,Answer,UserAnswer
from .forms import QuestionForm,UserResponseForm

# Create your views here.
import decimal

@login_required()

def match_all(request):
    question_form =UserResponseForm()
    queryset = Question.objects.all().order_by('-timestamp')

    question_instance = queryset.order_by("?")[0]

    context = {'question_form':question_form,
               'question_instance':question_instance}

    return render(request,'questions/match_all.html',context)



def home(request):
    if request.user.is_authenticated:
        form = UserResponseForm(request.POST or None)

        # try:
        #     user_answer = UserAnswer.objects.get(user=request.user, question=instance)
        # except UserAnswer.DoesNotExist:
        #     user_answer = UserAnswer()
        # except UserAnswer.MultipleObjectsReturned:
        #     user_answer = UserAnswer.objects.filter(user=request.user, question=instance)[0]
        # except:
        #     user_answer = UserAnswer()
        if form.is_valid():
            print(form.cleaned_data)
            question_id = form.cleaned_data.get('question_id') #form.cleaned_data['question_id']
            answer_id = form.cleaned_data.get('answer_id')
            importance_level = form.cleaned_data.get('importance_level')
            question_instance = Question.objects.get(id=question_id)
            answer_instance = Answer.objects.get(id=answer_id)
            user_answer = UserAnswer()
            user_answer.user = request.user
            user_answer.question = question_instance
            user_answer.my_answer = answer_instance
            user_answer.my_answer_importance = importance_level
            user_answer.save()
            print (answer_instance.text)
            print (question_instance.text)
            next_q = Question.objects.all().order_by("?").first()
            return redirect("question_single", id=next_q.id)

        queryset = Question.objects.all().order_by('-timestamp')
        instance = queryset[0]



        context = {"instance":instance,
			        "form": form,
                         }
            # 'user_answer':user_answer,

        return render(request, "questions/home.html", context)
    else:
        raise Http404


# def single(request, id):
#     if request.user.is_authenticated:
#         queryset = Question.objects.all().order_by('-timestamp')
#         instance = get_object_or_404(Question, id=id)
#         try:
#             user_answer = UserAnswer.objects.get(user=request.user, question=instance)
#         except UserAnswer.DoesNotExist:
#             user_answer = UserAnswer()
#         except UserAnswer.MultipleObjectsReturned:
#             user_answer = UserAnswer.objects.filter(user=request.user, question=instance)[0]
#         except:
#             user_answer = UserAnswer()
#
#         form = UserResponseForm(request.POST or None)
#         if form.is_valid():
#             print (form.cleaned_data)
#             # print request.POST
#             question_id = form.cleaned_data.get('question_id')  # form.cleaned_data['question_id']
#             answer_id = form.cleaned_data.get('answer_id')
#
#             importance_level = form.cleaned_data.get('importance_level')
#             their_importance_level = form.cleaned_data.get('their_importance_level')
#             their_answer_id = form.cleaned_data.get('their_answer_id')
#
#
#             question_instance = Question.objects.get(id=question_id)
#             answer_instance = Answer.objects.get(id=answer_id)
#             # their_answer_instance = Answer.objects.get(id=their_answer_id)
#
#             user_answer.user = request.user
#             user_answer.question = question_instance
#             user_answer.my_answer = answer_instance
#             user_answer.my_answer_importance = importance_level
#             if their_answer_id != -1:
#                 their_answer_instance = Answer.objects.get(id=their_answer_id)
#                 user_answer.their_answer = their_answer_instance
#                 user_answer.their_importance = their_importance_level
#             else:
#                 user_answer.their_answer = None
#                 user_answer.their_importance = "Not Important"
#             user_answer.save()
#
#
#
#
#             next_q = Question.objects.all().order_by("?").first()
#             return redirect("question_single", id=next_q.id)
#
#
#
#         context = {
#             "form": form,
#             "instance": instance,
#             # "user_answer": user_answer,
#             # "queryset": queryset
#         }
#         return render(request, "questions/single.html", context)
#     else:
#         raise Http404

def single(request, id):
    if request.user.is_authenticated:

        queryset = Question.objects.all().order_by('-timestamp')
        instance = get_object_or_404(Question, id=id)

        try:
            user_answer = UserAnswer.objects.get(user=request.user, question=instance)
        except UserAnswer.DoesNotExist:
            user_answer = UserAnswer()
        except UserAnswer.MultipleObjectsReturned:
            user_answer = UserAnswer.objects.filter(user=request.user, question=instance)[0]
        except:
            user_answer = UserAnswer()

        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print (form.cleaned_data)
            # print request.POST

            question_id = form.cleaned_data.get('question_id')  # form.cleaned_data['question_id']

            answer_id = form.cleaned_data.get('answer_id')
            importance_level = form.cleaned_data.get('importance_level')

            their_importance_level = form.cleaned_data.get('their_importance_level')
            their_answer_id = form.cleaned_data.get('their_answer_id')

            question_instance = Question.objects.get(id=question_id)
            answer_instance = Answer.objects.get(id=answer_id)

            user_answer.user = request.user
            user_answer.question = question_instance
            user_answer.my_answer = answer_instance
            user_answer.my_answer_importance = importance_level
            if their_answer_id != -1:
                their_answer_istance = Answer.objects.get(id=their_answer_id)
                user_answer.their_answer = their_answer_istance
                user_answer.their_importance = their_importance_level
            else:
                user_answer.their_answer = None
                user_answer.their_importance = "Not Important"
            user_answer.save()

            next_q = Question.objects.all().order_by("?").first()
            return redirect("question_single", id=next_q.id)

        context = {
            "form": form,
            "instance": instance,
            "user_answer": user_answer,
            # "queryset": queryset
        }
        return render(request, "questions/single.html", context)
    else:
        raise Http404





