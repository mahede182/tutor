from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, max_length=50)

    class Meta:
        ordering = ['id']