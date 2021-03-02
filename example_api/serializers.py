from rest_framework import serializers

from .models import Administrator, Poll, Questions


class AdministratorSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=32)
    token = serializers.CharField(max_length=32)


class PollSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField()

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('start_date') and validated_data.get('start_date') != instance.start_date:
            raise serializers.ValidationError('You can not change start date')
        instance.title = validated_data.get('title', instance.title)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class QuestionsSerializer(serializers.Serializer):
    poll_id = serializers.RelatedField(source='Poll', read_only=True)
    question_id = serializers.IntegerField()
    question = serializers.CharField()
    question_type = serializers.RelatedField(source='QuestionsTypes', read_only=True)

    def create(self, validated_data):
        return Questions.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.poll_id = validated_data.get('poll_id', instance.poll_id)
        instance.question_id = validated_data.get('question_id', instance.question_id)
        instance.question = validated_data.get('question', instance.question)
        instance.question_type = validated_data.get('question_type', instance.question_type)
        instance.save()
        return instance
