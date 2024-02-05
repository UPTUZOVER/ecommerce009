from django.db import models




class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=133, unique=True)
    description = models.TextField(max_length=444, blank=True)
    cat_image = models.ImageField(upload_to='photo/category', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

























