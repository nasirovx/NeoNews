from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)
    is_favorite = models.BooleanField('Is Favorite', default=False)
    image = models.ImageField('Image', upload_to='news_images/', blank=True, null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    
    def __str__(self):
        return self.name