from django.db import models


class Administrator(models.Model):
    login = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=32)
    token = models.CharField(max_length=32)


class Poll(models.Model):
    poll_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()


class QuestionsTypes(models.Model):
    type_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256)


class Questions(models.Model):
    poll_id = models.ForeignKey(Poll, related_name='polls_questions', on_delete=models.CASCADE)
    question_id = models.IntegerField()
    question = models.TextField()
    question_type = models.ForeignKey(QuestionsTypes, related_name='questions_types', on_delete=models.CASCADE)


class Users(models.Model):
    token = models.CharField(max_length=32, primary_key=True)


class Answers(models.Model):
    token = models.ForeignKey(Users, related_name='users_tokens', on_delete=models.CASCADE)
    poll_id = models.ForeignKey(Poll, related_name='polls_answers', on_delete=models.CASCADE)
    question_id = models.IntegerField()
    answer = models.TextField()


