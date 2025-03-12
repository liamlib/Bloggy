from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, default="My title") #When we create a field, which is mandatory, we should also provide a default
    subheading = models.CharField(max_length=255 , null= True, blank=True)
    author = models.CharField(max_length=190, null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)
    content = HTMLField()

    def __str__(self):
        return f"Post {self.title} from {self.author}"

    class Meta:
        verbose_name_plural = "Posts"

class New(models.Model):
    title = models.CharField(max_length= 255, default="my title")
    subheading = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=190, null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)
    content = HTMLField()

    def __str__(self):
        return f"Post {self.title} from {self.author}"

    class Meta:
        verbose_name_plural = "New"

class Posts(models.Model):
    title = models.CharField(max_length= 255, default="my title")
    subheading = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=190, null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)
    content = HTMLField()

    def __str__(self):
        return f"Post {self.title} from {self.author}"




