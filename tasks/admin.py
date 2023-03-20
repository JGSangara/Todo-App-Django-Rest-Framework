from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'due', 'completed', 'owner')
    list_display_links = ('id', 'title')
    list_filter = ('completed', 'owner')
    search_fields = ('title', 'owner__email')
    list_per_page = 25
