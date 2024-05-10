from django.contrib import admin

from apps.classroom.models import ClassRoom


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    pass
