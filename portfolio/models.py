from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.pk:  # Check if the instance is being updated
            original_order = Category.objects.get(pk=self.pk).order
            if self.order != original_order:
                # Get all categories with the same order
                conflicting_categories = Category.objects.filter(order=self.order).exclude(pk=self.pk)
                for category in conflicting_categories:
                    # Swap the order of the conflicting category with the current one
                    category.order = original_order  # Set the conflicting category's order to the original
                    # Use update instead of save to avoid recursion
                    Category.objects.filter(pk=category.pk).update(order=original_order)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100 , null=True, blank=True)    
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='portfolio/images/' , null=True, blank=True)
    url = models.URLField(null=True,blank=True)
    isVideo = models.BooleanField(default=False)
    isFeatured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

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

    

