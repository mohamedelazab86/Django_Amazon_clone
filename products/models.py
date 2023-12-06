from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    flag_type=[ 
        ('New','New'),
        ('Sale','Sale'),
        ('Feature','Feature'),
        ]

    name=models.CharField(max_length=120,verbose_name=_('name_prouct'))
    flag=models.CharField(_('flag'),max_length=20,choices=flag_type)
    price=models.DecimalField(_('price'),max_digits=6,decimal_places=2)
    image=models.ImageField(_('image'),upload_to='image_product %y-%m-%d')
    subtitle=models.TextField(_('subtitle'),max_length=1000)
    descritions=models.TextField(_('description'),max_length=50000)

    slug=models.SlugField(null=True,blank=True,verbose_name=('slug'))
    tags = TaggableManager()
    sku=models.IntegerField(verbose_name=_('sku'))
    brand=models.ForeignKey('Brand',on_delete=models.SET_NULL,null=True,verbose_name=_('brand'))



    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=self.name
        super(Product,self).save(*args,**kwargs)

class ImageProduct(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='imageproduct_product',verbose_name=_('product'))
    image=models.ImageField(upload_to='photo_product%y-%m-%d',verbose_name=_('image'))
    
    def __str__(self):
        return str(self.product)
    
class Brand(models.Model):
    name=models.CharField(max_length=120,verbose_name=_('name_brand'))
    image=models.ImageField(upload_to='photo_brand%y-%m-%d',verbose_name=_('image_brand'))
    slug=models.SlugField(null=True,blank=True,verbose_name=_('slug'))

    
    def __str__(self) :
        return self.name
    def save(self,*args,**kwargs):
        self.slug=self.name
        super(Brand,self).save(*args,**kwargs)
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,verbose_name=_('user'))
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='review_product',verbose_name=_('product'))
    review=models.TextField(max_length=200,verbose_name=_('review'))
    publish_date=models.DateTimeField(default=timezone.now)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,6)],verbose_name=_('rate'))

    def __str__(self):
        return f'{self.user}  --- {self.review}'
    




    



