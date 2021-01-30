from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.start_date > self.end_date:
            raise ValidationError(
                    'Start date can not be over end date'
                )

    def get_active():
        today = timezone.now().date()
        active_quizzes = Quiz.objects.filter(start_date__gte=today)
        return active_quizzes
    

class Question(models.Model):
    question_types = (
        ('radio', 'radio'),
        ('checkbox', 'checkbox'),
        ('text', 'text'),
    )
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000)
    question_type = models.CharField(
        max_length=8,
        choices=question_types,
        default=_('radio')
    )

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"

    def __str__(self):
        return self.choice_text


class AnswerTracker(models.Model):
    customer = models.IntegerField(verbose_name=_('customer_id'))
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE, blank=True, null=True)
    answer_text = models.TextField(blank=True)

    class Meta:
        verbose_name = "Answer Tracker"
        verbose_name_plural = "Answers Tracker"

    def clean(self):
        super().clean()
        if not any([self.choice_id, self.answer_text]):
            raise ValidationError(
                    'Answers choice or text fields must be filled'
                )

    def __str__(self):
        return f'{self.customer} - {self.question_id} - {self.choice_id or self.answer_text}'
