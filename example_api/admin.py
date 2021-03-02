from django.contrib import admin

from .models import Administrator, Poll, QuestionsTypes, Questions, Users, Answers


admin.site.register(Administrator)
admin.site.register(Poll)
admin.site.register(QuestionsTypes)
admin.site.register(Questions)
admin.site.register(Users)
admin.site.register(Answers)
