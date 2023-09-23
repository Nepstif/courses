from django.urls import path

from . import views

app_name = "lesson"


urlpatterns = [
    path('list/',
         views.LessonListView.as_view(),
         name='lesson_list'),
    path('lesson_product/',
         views.LessonProductView.as_view(),
         name='lesson_product'),
]