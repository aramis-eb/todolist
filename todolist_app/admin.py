from django.contrib import admin
from .models import Priority, Todo


class PriorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')


admin.site.register(Priority, PriorityAdmin)
admin.site.register(Todo)
