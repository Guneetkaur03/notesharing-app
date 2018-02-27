from django.db import models
from django.utils import timezone


class details_notes(models.Model):
    subject = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    teacher = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
