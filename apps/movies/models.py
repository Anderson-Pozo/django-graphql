from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        order_with_respect_to = 'name'


class Movie(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    actor = models.ForeignKey(
        Actor, related_name='movies', on_delete=models.CASCADE
    )
    published_date = models.DateField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'title'
