from django.contrib import admin
from .models import Tasks

# Register your models here.
#admin.site.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = (['title', 'user'])
    readonly_fields=['created']

admin.site.register(Tasks, TasksAdmin)

def __str__(self):
    return self.title

