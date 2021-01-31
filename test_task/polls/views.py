from typing import List, Dict

from rest_framework.views import APIView, Response, Request
from rest_framework import status
from django.shortcuts import get_list_or_404

from .models import Quiz, Question, AnswerTracker
from .serializer import QuizSerializer, QuestionSerializer, AnswerSerializer, AnswerTrackerSerializer


class QuizzesListView(APIView):
    def get(self, request: Request) -> Response:
        active_quizzes_qs = Quiz.get_active()
        serialized_data = QuizSerializer(active_quizzes_qs, many=True)
        print(serialized_data.data)
        return Response(serialized_data.data)


class QuizDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        quiz_qs = get_list_or_404(Question, quiz_id=pk)
        serialized_data = QuestionSerializer(quiz_qs, many=True)
        return Response(serialized_data.data)


class AnswerTrakerView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        parsed_answers: List[dict] = self.parse_request(request, pk)
        serialized_answers = AnswerTrackerSerializer(data=parsed_answers, many=True)
        if serialized_answers.is_valid(raise_exception=True):
            serialized_answers.save()
            return Response(serialized_answers.data, status=status.HTTP_201_CREATED)
        return Response(serialized_answers.errors, status=status.HTTP_400_BAD_REQUEST)

    def parse_request(self, request: Request, pk: int) -> List[dict]:
        parsed_answers: List[dict] = []
        for question in request.data['answers']:
            answer: dict = {}
            answer['quiz_id'] = pk
            answer['customer'] = request.data['customer']
            answer['question_id'] = question['id']
            answer['answer_text'] = question.get('answer_text', '')
            if question.get('choices'):
                for choice in question['choices']:
                    answer['choice_id'] = choice
                    parsed_answers.append(answer.copy())
            else:
                parsed_answers.append(answer.copy())
        return parsed_answers


class ReportView(APIView):
    def get(self, request: Request) -> Response:
        customer: str = request.query_params.get('customer')
        report = get_list_or_404(AnswerTracker, customer=customer)
        serialized_report = AnswerSerializer(report, many=True)
        parsed_report = self.parse_report(serialized_report.data)
        return Response(parsed_report)

    def parse_report(self, serialized_report: List[dict]) -> List[dict]:
        quizzes: set = set(answer['quiz'] for answer in serialized_report)
        parsed_report: dict = {quiz: [] for quiz in quizzes}
        for answer in serialized_report:
            parsed_report[answer.pop('quiz')].append(answer)
        return parsed_report
