from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100 , null=True, blank=True)    
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='portfolio/images/' , null=True, blank=True)
    url = models.URLField(null=True,blank=True)
    isVideo = models.BooleanField(default=False)
    isFeatured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.url: 
            self.isVideo = True
        else:
            self.isVideo = False
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        if self.title is None:
            return f'{self.id} no title'
        return self.title

    

