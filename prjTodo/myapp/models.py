from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    description = models.TextField()
    createdBy = models.CharField(max_length=100)
    completed = models.BooleanField()

    def __str__(self) -> str:
        return self.name

