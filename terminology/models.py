from django.db import models
from django.urls import reverse


class Term(models.Model):
    name = models.CharField("Name", max_length=512, unique=True)
    explanation = models.TextField("Explanation")
    parents = models.ManyToManyField('Term', related_name='children')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('term_details', kwargs={'term_pk': self.pk})
