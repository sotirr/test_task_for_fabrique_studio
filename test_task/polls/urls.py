from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.QuizzesListView.as_view(), name='quizzes_list'),
    path('<int:quiz_id>/', views.QuizDetailView.as_view(), name='quizzes_detail'),
    path('<int:quiz_id>/answers/', views.AnswerTrakerView.as_view()),
    path('report/', views.ReportView.as_view(), name='report'),
]
