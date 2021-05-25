from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    dop = models.DateField(verbose_name="publicationDate")
    content = TextField()

    def __str__(self) -> str:
        return self.title
    