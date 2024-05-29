from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DesimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image_field = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    count = models.IntegerField()
    
    
    def __str__(self):
        return f'{self.name} - {self.description}'
    
    
class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    item = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    
    
    def __str__(self):
        return f"Order {self.id}: {self.name} - {self.item}"
    

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_dleete=modesl.CASCADE)
    product = models.ForeignKey(Product, on_delete=mmodels.CASCADE)
    count = models.IntegerField()
    