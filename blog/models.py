from django.db import models

# Create your models here.
# create a Blog models
    # title
    # pub_date
    # body
    # image
class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
   
# Add the Blog app to settings
# create a makemigration
# migrate
# add to the admin
