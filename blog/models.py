#from __future__ import unicode_literals

#from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

#Post = name of model, always start class name w/ uppercase letter!
class Post(models.Model): #object, class=keyword that indicates that we are defining an object
 #models.Model= post is a django model, so it savews it as a database
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
 #need to indent everything under the class bc python sensitive to whitespace
 
