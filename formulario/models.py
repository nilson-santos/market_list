from django.db import models 
import uuid 

# Create your models here.


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category)
    
    class Meta:
        ordering = ['category']


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=20)
    amount = models.CharField(blank=True, max_length=30)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.item)
