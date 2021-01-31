from rest_framework.serializers import ModelSerializer, SerializerMethodField, Serializer, StringRelatedField

from rest_framework import serializers

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

'''
class AnswerSerializer(Serializer):
    quiz = serializers.SerializerMethodField('get_quiz_title')

    def get_quiz_title(self, obj):
        quiz_title: str = obj.quiz_id.title
        questions = AnswerTracker.objects.all().filter(quiz_id=obj.quiz_id.id, customer=obj.customer)
        serialized_questions = AnsweredQuestionsSerializer(questions, many=True)
        return {quiz_title: serialized_questions.data}
'''

class AnswerTrackerSerializer(ModelSerializer):
    class Meta:
        model = AnswerTracker
        fields = '__all__'


class AnswerSerializer(Serializer):
    quiz = serializers.SerializerMethodField('get_quiz_title')
    question = serializers.SerializerMethodField('get_question_text')
    answer_text = serializers.CharField()
    choice = serializers.SerializerMethodField('get_choice_text')

    def get_quiz_title(self, obj):
        return obj.quiz_id.title
    
    def get_question_text(self, obj):
        return obj.question_id.question_text
    
    def get_choice_text(self, obj):
        return obj.choice_id.choice_text if obj.choice_id else None
    


class AnsweredQuestionsSerializer(ModelSerializer):

    class Meta:
        model = AnswerTracker
        fields = ['question_id', 'choice_id', 'answer_text']



