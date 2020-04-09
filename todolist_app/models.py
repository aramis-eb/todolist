from django.db import models
from django.conf import settings


class Priority(models.Model):

    name = models.CharField(max_length=20)
    order = models.IntegerField()

    class Meta:
        verbose_name_plural = "Priorities"

    def __str__(self):
        return 'id: {} - {} (order {})'.format(
            self.id,
            self.name,
            self.order,
        )


class Todo(models.Model):

    tittle = models.CharField(max_length=20)
    description = models.TextField()
    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='asigned',
    )
    done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created',
        )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='updated',
        )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,

    )
