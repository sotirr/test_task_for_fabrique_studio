from django.urls import path

from .views import QuizzesListView, QuizDetailView, AnswerTrakerView, ReportView

app_name = 'polls'
urlpatterns = [
    path('', QuizzesListView.as_view(), name='quizzes_list'),
    path('<int:pk>/', QuizDetailView.as_view(), name='quizzes_detail'),
    path('<int:pk>/answer/', AnswerTrakerView.as_view()),
    path('report/', ReportView.as_view(), name='report'),
]
