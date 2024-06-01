from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class todolist(models.Model):
    class status(models.TextChoices):
        not_started = "NOT STARTED", _("Not Started")
        ongoing = "ONGOING", _("Ongoing")
        done = "DONE", _("Done")
        
    title = models.CharField(max_length=200)
    description = models.TextField()
    task_status = models.CharField(
        max_length=20,
        choices=status.choices,
        default=status.not_started,
        
    )
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'todolist'