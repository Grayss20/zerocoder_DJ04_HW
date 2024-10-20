from django.db import models

# Create your models here.


class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    review = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        