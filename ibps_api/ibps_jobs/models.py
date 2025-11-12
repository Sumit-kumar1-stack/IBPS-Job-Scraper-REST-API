from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    posted_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
