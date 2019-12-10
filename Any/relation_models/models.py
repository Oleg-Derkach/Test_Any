from django.db import models
from django.shortcuts import reverse
from django.conf import settings


class User(models.Model):
    name = models.CharField(max_length=20)
    address = models.OneToOneField('Address', related_name='shipping_address', 
        on_delete=models.SET_NULL, blank=True, null=True)  
  
    def __str__(self):
        return self.name
    

class Address(models.Model): 

    first_last_name = models.CharField(max_length=50, verbose_name="Заказчик")
    city_region = models.CharField(max_length=255, blank=True)
    delivery_address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, default=None, null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа", null=True)
    comments = models.TextField(blank=True)
    
    def __str__(self):
        return self.first_last_name   
  
    
class Account(models.Model):
    
    address = models.OneToOneField(Address, on_delete = models.CASCADE, default=' ')
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20) 
    
    def __str__(self):
        return self.login 
  
class Item(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title   
    class Meta:    
        verbose_name_plural = "Товар" 
        
class ItemsQuantity(models.Model):
    product_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1) 
    
    def __str__(self):
        return '{} pcs. {}'.format(self.quantity, self.product_item.title)
    class Meta:    
        verbose_name_plural = "Товар и колличество" 
 
       
class ProductCase(models.Model):
    product_case = models.ForeignKey(ItemsQuantity, on_delete=models.CASCADE)
    def __str__(self):
        return   '{} pcs. {}'.format(self.product_case.quantity, self.product_case.product_item.title )
    class Meta:    
        verbose_name_plural = "Коробка с товаром"   
      
        
class Order(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(ProductCase)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)    
    class Meta:    
        verbose_name_plural = "Заказ"    
        
        
        
class Book(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    authors = models.ManyToManyField('Author', through='Authored')
    quantity = models.IntegerField(default=1) 
          
        
class Author(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    books = models.ManyToManyField('Book', through='Authored')
    

class Authored(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)      
        
        
class Person(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name 

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, related_name='groups')    
    def __str__(self):
        return self.name 
        
        
        
        
        
        