from django.db import models


class profile(models.Model):
    """Users' profiles"""

    name = models.CharField(max_length=120)
    description = models.TextField(default='default text')
    
    def __unicode__(self):
        """Returns the profile's name to the admin tool"""
        return self.name
