from django.urls import path

from .views import AdministratorView, PollView, QuestionsView


app_name = 'example_api'

urlpatterns = [
    path('login/', AdministratorView.as_view()),
    path('poll/', PollView.as_view()),
    path('poll/<int:poll_id>', PollView.as_view()),
    path('question/', QuestionsView.as_view()),
    path('question/<int:poll_id>/<int:question_id>', QuestionsView.as_view())
]