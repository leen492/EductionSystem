from django.db import models
class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    level=models.CharField(max_length=45)
    def __str__(self):
         return self.title


