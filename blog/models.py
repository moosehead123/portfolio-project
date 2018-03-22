from django.db import models

# Create a blog models
# title
# pub_date
# body
# image

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Add Blog app to the settings

# Create migration

# Migrate

# Add to the admin
