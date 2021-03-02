from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from uuid import uuid4

from .models import Administrator, Poll, Questions, QuestionsTypes
from .serializers import AdministratorSerializer, PollSerializer, QuestionsSerializer


class AdministratorView(APIView):
    def post(self, request):
        login = request.data.get('login')
        password = request.data.get('password')
        try:
            account = Administrator.objects.get(login=login, password=password)
        except:
             return Response({'error': 'provide correct login or password'})
        serializer = AdministratorSerializer(account)
        account.token = uuid4()
        return Response({'token': serializer.data['token']})


class PollView(APIView):
    def post(self, request):
        poll = request.data.get('poll')
        serializer = PollSerializer(data=poll)
        if serializer.is_valid(raise_exception=True):
            poll_saved = serializer.save()
        return Response({"success": "Poll '{}' created successfully".format(poll_saved.title)})

    def put(self, request, poll_id):
        saved_poll = get_object_or_404(Poll.objects.all(), poll_id=poll_id)
        data = request.data.get('poll')
        serializer = PollSerializer(instance=saved_poll, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            poll_saved = serializer.save()
        return Response({
            "success": "Poll '{}' updated successfully".format(poll_saved.title)
        })

    def delete(self, request, poll_id):
        poll = get_object_or_404(Poll.objects.all(), poll_id=poll_id)
        poll.delete()
        return Response({"message": "Poll with id `{}` has been deleted.".format(poll_id)}, status=204)


class QuestionsView(APIView):
    def post(self, request):
        question = request.data.get('question')
        poll = get_object_or_404(Poll.objects.all(), poll_id=question.get('poll_id'))
        type_id = get_object_or_404(QuestionsTypes.objects.all(), type_id=question.get('question_type'))
        question['poll_id'] = poll
        question['question_type'] = type_id
        serializer = QuestionsSerializer(data=question)
        if serializer.is_valid(raise_exception=True):
            question_saved = serializer.save()
        return Response({"success": "Question '{}' created successfully".format(question_saved.title)})

    def put(self, request, poll_id, question_id):
        saved_question = get_object_or_404(Poll.objects.all(), poll_id=poll_id, question_id=question_id)
        data = request.data.get('question')
        serializer = QuestionsSerializer(instance=saved_question, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            question_saved = serializer.save()
        return Response({
            "success": "Question '{}' updated successfully".format(question_saved.title)
        })

    def delete(self, request, poll_id, question_id):
        question = get_object_or_404(Poll.objects.all(), poll_id=poll_id, question_id=question_id)
        question.delete()
        return Response({"message": "Question with id `{}-{}` has been deleted.".format(poll_id, question_id)}, status=204)

    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response({"polls": serializer.data})