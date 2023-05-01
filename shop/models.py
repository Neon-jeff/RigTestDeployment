from django.db import models

# Create your models here.

class ShopItem(models.Model):
    Item_Type=(
        ('merch','merch'),
        ('book','book'),
        ('limited','limited'),
        ('work-book','work-book')
    )
    item_name=models.CharField(max_length=500)
    item_type=models.CharField(max_length=300,choices=Item_Type)
    item_price=models.IntegerField(default=0)
    item_link=models.URLField(blank=True)
    date_added=models.DateField(auto_now_add=True)
    item_image=models.ImageField(upload_to='shop-images',null=True,blank=True)
    item_desc=models.TextField(max_length=2000,blank=True,default='')
    def __str__(self):
        return self.item_name
