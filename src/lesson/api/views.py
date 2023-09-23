from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from lesson.api.serializers import LessonViewerSerializer
from lesson.models import LessonViewer
from product.models import Product


class LessonListView(APIView):
    """
    Получение списка уроков по которым у пользователей есть доступ.
    """
    def get(self, request: Request) -> Response:
        """

        :param Request  request: Объект запроса
        :return:
        """

        products = Product.objects.select_related("user").filter(access=True)
        user_list_id = []
        for product in products:
            user_list_id.append(product.user)

        lesson_list_db = LessonViewer.objects.filter(user__in=user_list_id)

        serializer = LessonViewerSerializer(lesson_list_db, many=True)
        data = serializer.data

        return Response(data)

class LessonProductView(APIView):
    """
    Получение списка уроков по конкретному продукту и по которым у пользователей есть доступ.
    """

    def get(self, request: Request, name:str) -> Response:
        """

        :param Request  request:Объект запроса
        :param name: Название курса
        :return:
        """

        products = Product.objects.filter(access=True)
        user_list_id = []
        for product in products:
            user_list_id.append(product.user)



        lesson_list_db = LessonViewer.objects.select_related("users", "lessons").filter(
            user__in=user_list_id, lesson=name
        )

        serializer = LessonViewerSerializer(lesson_list_db, many=True)
        data = serializer.data

        return Response(data)