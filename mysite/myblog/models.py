from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Post(models.Model):

    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    # Return unicode title
    def __unicode__(self):
        return self.title

## Many To Many Relationship
##     Posts have many Categories, Categories have many Posts
##     Note: must save Category before adding Post(s)
class Category(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    ## Relationship
    posts = models.ManyToManyField(Post, blank=True, null=True, related_name='categories')
    #posts = models.OneToOneField(Post, primary_key=True)

    # Return unicode name
    def __unicode__(self):
        return self.name
