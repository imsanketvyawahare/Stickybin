from django.db import models


class Sticky(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField()
    slug = models.CharField(max_length=7)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
