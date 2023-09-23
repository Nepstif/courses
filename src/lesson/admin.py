"""
Функции панели управления для приложения "Урок".
"""

from django.contrib import admin

from lesson.models import Lesson, LessonViewer


class LessonInLine(admin.TabularInline):
    model = Lesson.product.through


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [
        LessonInLine,
    ]

    list_display = (
        "name",
        "video",
        "duration",

    )

    search_fields = ("name", "product")

    list_filter = (
        "created_at",
        "updated_at",
    )
    def get_queryset(self, request):
        return Lesson.objects.prefetch_related("product")

@admin.register(LessonViewer)
class LessonViewerAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "lesson",
        "viewed_time",
        "viewed"
    )

    def get_queryset(self, request):
        return LessonViewer.objects.select_related("user", "lesson")