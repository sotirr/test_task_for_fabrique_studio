from rest_framework.serializers import ModelSerializer

from .models import Quiz, Question, AnswerTracker, Choice


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']


class QuestionSerializer(ModelSerializer):
    choice_set = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_type', 'choice_set']


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = AnswerTracker
        fields = '__all__'
