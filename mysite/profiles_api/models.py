from django.db import models
# each class has own table in database.

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date_postde = models.DateTimeField(auto_now_add=True)