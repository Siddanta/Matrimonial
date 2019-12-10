from .models import QuestionAnswer,Question,Answer
from django import forms

Level_choices= (('Mandatory','Mandatory'),
                ('Very Important','Very Important'),
                ('Somewhat  Important','Somewhat Important'),
                ('Not Important','Not Important'),

                )


class UserResponseForm(forms.Form):
    question_id = forms.IntegerField()
    answer_id = forms.IntegerField()
    importance_level = forms.ChoiceField(choices=Level_choices)
    their_answer_id = forms.IntegerField()
    their_importance_level = forms.ChoiceField(choices=Level_choices)

    def clean_question_id(self):
        question_id = self.cleaned_data.get('question_id')
        try:
            obj = Question.objects.get(id=question_id)
        except:
            raise forms.ValidationError('There was an error with the question. Please try again.')
        return question_id

    def clean_answer_id(self):
        answer_id = self.cleaned_data.get('answer_id')
        try:
            obj = Answer.objects.get(id=answer_id)
        except:
            raise forms.ValidationError('There was an error with the answer. Please try again.')
        return answer_id

    def clean_their_answer_id(self):
        their_answer_id = self.cleaned_data.get('their_answer_id')
        try:
            obj = Answer.objects.get(id=their_answer_id)
        except:
            if their_answer_id == -1:
                return their_answer_id
            else:
                raise forms.ValidationError(
                    'There was an error with the answer you provided for them. Please try again.')
        return their_answer_id


class QuestionForm(forms.ModelForm):

    class Meta:
        model = QuestionAnswer

        labels = {'Answer1': 'what family affluence you prefer?',
                    'Answer2':'what family values you prefer?'}
        fields = ['Answer1','Answer2']