from django.contrib import admin
from .models import todoList
# Register your models here.

@admin.register(todoList)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','created_at','completed']
