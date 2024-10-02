from django.db import models

# Define a Django model for Feature
class Feature(models.Model):
    # Define fields directly in the class
    name = models.CharField(max_length=100)  # Name field (max_length is required for CharField)
   
    details = models.CharField(max_length=500)  # Details field (you can use TextField for longer text)














