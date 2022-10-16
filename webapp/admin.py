from django.contrib import admin
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    list_filter = ('id', 'title', 'description', 'created_at')
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Task, TaskAdmin)

