from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_maker = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Phone_no = models.IntegerField()
    Address = models.TextField(max_length=100)




CATEGORY_CHOICES = (
    ("egg", "egg"),
    ("eggless", "eggless")
)


class cake(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    description = models.TextField()
    picture = models.ImageField()


class orderplaced(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    description = models.TextField()
    picture = models.ImageField()
    order_status = models.IntegerField(default=False)


class payment(models.Model):
    shipping_address = models.TextField(null=True)
    price = models.FloatField(null=True)
    card_number = models.IntegerField(null=True)
    cvv = models.IntegerField(null=True)
    date = models.DateField(null=True)
    delivery_status = models.BooleanField(default=False, null=True)
    payment_status = models.BooleanField(default=False, null=True)
