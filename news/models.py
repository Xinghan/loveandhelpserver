from django.db import models

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Entry(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created= models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now_add=True)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return self.title.encode('utf-8')

    class Meta:
        verbose_name = "News Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
    
