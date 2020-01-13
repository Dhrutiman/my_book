from django.db import models

# Create your models here.
class Search(models.Model):
    search=models.CharField(max_length=800)
    created= models.DateTimeField(auto_now=True)
    type=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural ="Searches"