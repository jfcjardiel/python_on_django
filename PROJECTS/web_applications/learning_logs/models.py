from django.db import models

#Here we are going to build the data models of our app
#The each one of the data is a class

#Each one of the user is going to create a topic
#It inherits the models.Model Class
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text