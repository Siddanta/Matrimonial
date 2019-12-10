from django.contrib.auth import get_user_model

from questions.models import UserAnswer, Question
from decimal import Decimal
from django.db.models import Q
#accounts app
from accounts.models import UserProfileModel





# def get_match(user_a,user_b):
#     user_a_answer = UserAnswer.objects.filter(user=user_a)[0]
#     user_b_answer = UserAnswer.objects.filter(user=user_b)[0]
#     if user_a_answer.question.id == user_b_answer.question.id:
#         user_a_value = user_a_answer.my_answer
#         user_a_pref = user_a_answer.their_answer
#         user_b_value = user_b_answer.my_answer
#         user_b_pref = user_b_answer.their_answer
#         user_b_total_awarded = 0
#         user_a_total_awarded = 0
#         if user_a_value == user_b_pref:
#             user_b_total_awarded += user_b_answer.their_points
#             print( str(user_a) + ' fits for ' + str(user_b))
#         if user_a_pref == user_b_value:
#             user_a_total_awarded += user_a_answer.their_points
#             print(str(user_b) + ' fits for ' + str(user_a))
#         if user_a_value == user_b_pref and user_a_value == user_b_answer:
#             print ('MAtched Succesfully ')
#         print(user_a, user_a_total_awarded)
#         print(user_b, user_b_total_awarded)
#     else:
#         print('mistake')
#
#
# get_match(sid, susan)
# get_match(sid,users[4])
# get_match(susan,users[4])

def get_match(user_a,user_b):
    q1 = Q(useranswer__user=user_a)
    q2 = Q(useranswer__user=user_b)
    question_set = Question.objects.filter(q1 | q2).distinct()
    print(user_a)
    print(user_b)
    # question_set1 = Question.objects.filter(q1)
    # question_set2 = Question.objects.filter(q2)
    # question_set = (question_set1 | question_set2).distinct()
    a_points = 0
    b_points = 0
    a_total_points = 0
    b_total_points = 0
    questions_in_common = 0
    for question in question_set:
        try:
            a = UserAnswer.objects.get(user=user_a, question=question)
        except:
            a = None
        try:
            b = UserAnswer.objects.get(user=user_b, question=question)
        except:
            b = None
        if a and b:
            questions_in_common += 1
            if a.their_answer == b.my_answer:
                b_points += a.their_points
            b_total_points += a.their_points
            if b.their_answer == a.my_answer:
                a_points += b.their_points
            a_total_points += b.their_points

    if questions_in_common > 0:
        a_decimal = a_points / Decimal(a_total_points)
        b_decimal = b_points / Decimal(b_total_points)
        print (b_decimal)
        print(a_decimal)
        if a_decimal == 0:
            a_decimal = 0.000001
        if b_decimal == 0:
            b_decimal = 0.000001
        match_percentage = (Decimal(a_decimal) * Decimal(b_decimal)) ** (1 / Decimal(questions_in_common))
        return match_percentage, questions_in_common
    else:
        return 0.0, 0


# def get_match(user_a,user_b):
#     a_answers = UserAnswer.objects.filter(user=user_a)
#     b_answers = UserAnswer.objects.filter(user=user_b)
#     a_total_awarded = 0
#     a_points_possible = 0
#     num_question = 0
#     for a in a_answers:
#         print(a)
#         for b in b_answers:
#             if a.question.id == b.question.id:
#                 num_question +=1
#                 a_pref = a.their_answer
#                 b_answer = b.my_answer
#                 if a_pref == b_answer:
#                     a_total_awarded += a.their_points
#                     print(a_total_awarded)
#                 a_points_possible += a.their_points
#                 print(str(user_a) + ' has awarded '+ str(a_total_awarded) + ' of ' + str(a_points_possible) + ' to ' +str(user_b))
#     percent = a_total_awarded/Decimal(a_points_possible )
#     print(percent)
#     print(num_question)
#     if percent == 0:
#         percent = 0.000001
#     return percent, num_question

# def get_match(user_a,user_b):
#     a=get_points(user_a,user_b)
#     b=get_points(user_b,user_a)
#     #a[0] = decimal match value
#     no_of_question = b[1] #b[1]/a[1] =no of questions answered
#     match_decimal = (Decimal(a[0]) * Decimal(b[0]))**(1/Decimal(no_of_question))
#     return match_decimal, no_of_question

# a = get_points(sid,susan)
# b = get_points(susan,sid)

# match_percentage = "%.2f" % (Decimal(a[0]) * Decimal(b[0])) ** (1/Decimal(a[1]))
# (0.67*1)**(1/3.0)