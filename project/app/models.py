from django.db import models

# Create your models here.
class ItemInfo(models.Model):
    item_name=models.CharField(max_length=50)
    item_desc=models.CharField(max_length=50)
    item_price=models.IntegerField()
    item_image=models.ImageField(upload_to='image')
    item_file=models.FileField(upload_to='file')