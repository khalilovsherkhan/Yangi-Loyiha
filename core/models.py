from django.db import models
from django.urls import reverse
# Create your models here.

class Bulim(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class BulimData(models.Model):
    post_category = models.ForeignKey(Bulim, on_delete=models.CASCADE)
    post_title = models.CharField(max_length = 255)
    post_content = models.TextField()
    post_image = models.ImageField(upload_to='post-image/')
    post_hashtag = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.post_title
    def get_absolute_url(self):
        return reverse('bulim', kwargs={'pk': self.pk})

class Category(models.Model):
    title = models.CharField(max_length = 255)
    def __str__(self):
        return self.title

class Post(models.Model):
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_title = models.CharField(max_length = 255)
    post_content = models.TextField()
    post_image = models.ImageField(upload_to='post-image/')
    post_hashtag = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now=True)
#yana nima muammo
    def __str__(self):
        return self.post_title
    

    class Hudud(models.Model):
        hudud_title = models.CharField(max_length=200)
        hudud_info = models.TextField()
        hudud_image = models.ImageField(upload_to='hudud/')
        google_location = models.TextField()


        def __str__(self):
            return self.hudud_title


     


