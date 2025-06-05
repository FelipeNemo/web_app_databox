from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.title