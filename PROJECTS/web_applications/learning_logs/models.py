from datetime import datetime , timedelta
from django.db import models
from django.utils import timezone

#Here we are going to build the data models of our app
#The each one of the data is a class

#Each one of the user is going to create a topic
#It inherits the models.Model Class
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text

#For each one of the Topics, there must have an entry
class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."