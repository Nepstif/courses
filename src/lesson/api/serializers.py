from rest_framework import serializers

from lesson.models import Lesson, LessonViewer


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о уроках
    """

    class Meta:
        model = Lesson
        fields = [
            "name",
            "description",
            "access",
            "user",
        ]


class LessonViewerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о просмотренных уроках.
    """

    class Meta:
        model = LessonViewer
        fields = [
            "user",
            "lesson",
            "viewed_time",
            "viewed",
        ]
