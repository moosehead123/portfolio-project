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

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title + " (" + str(self.pub_date) + ")"

    def summary(self):
        return self.body[:100]


# Add Blog app to the settings

# Create migration

# Migrate

# Add to the admin
