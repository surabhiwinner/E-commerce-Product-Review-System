from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class ProfileChoices(models.TextChoices):
    USER = 'User' , 'User'
    ADMIN = 'Admin' , 'Admin'
   
AbstractUser


class Profile(AbstractUser):
    role = models.CharField(max_length=50,choices=ProfileChoices , default='User')
    

    def __str__(self):
        return f"{self.username} - {self.role}"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.SlugField(unique=True, editable=False)

    class Meta:
        abstract = True


class Product(BaseModel):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    

class ProductReview(BaseModel):
    product = models.ForeignKey(Product,related_name='revirews', on_delete=models.CASCADE)
    reviewer_name = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='reviewer')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.product.name} - {self.rating} stars"  
    class Meta:
        ordering = ['-review_date']
        verbose_name = 'Product Review'
        verbose_name_plural = 'Product Reviews'