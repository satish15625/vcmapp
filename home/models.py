from django.db import models

# Create your banner modee
class Banner(models.Model):
    banner_img = models.ImageField(upload_to='pics')
    banner_title = models.CharField(max_length=100)
    banner_desc = models.TextField() 
    banner_right_desc = models.TextField()
    read_more_desc =  models.TextField()
