from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from api.models import Class, User, Notice, PlayStoreInfo, Review, Edit


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = (
            'id', 'year', 'semester', 'code', 'name', 'professor', 'place', 'size', 'grade',
            'start1', 'end1', 'week1',
            'start2', 'end2', 'week2',
            'start3', 'end3', 'week3',
            'start4', 'end4', 'week4',
            'start5', 'end5', 'week5',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'uid', 'email', 'majorCode', 'studentId', 'sex', 'age',
        )


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = (
            'id', 'title', 'subtitle', 'body', 'created', 'writer',
        )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id', 'reviewClass', 'writer', 'body', 'created',
        )


class EditSerializer(serializers.ModelSerializer):
    editClassData = ClassSerializer(source='editClass', read_only=True)

    class Meta:
        model = Edit
        fields = (
            'id', 'year', 'semester', 'editClassData', 'writer', 'created', 'type', 'value', 'editClass','star',
        )


class PlayStoreInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayStoreInfo
        fields = (
            'id', 'versionName', 'versionCode',
        )
