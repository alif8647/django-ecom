from django.contrib.auth.models import User
from django.db import models

# Create your models here.
CHOICE_DISTRICT = (
    ('Kushtia', 'Kushtia'),
    ('Meherpur', 'Meherpur'),
    ('Rajbari', 'Rajbari'),
    ('Foridpur', 'Foridpur'),
    ('Sholkupa', 'Sholkupa'),
    ('Dhaka', 'Dhaka'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    postcode = models.IntegerField()
    thana = models.CharField(max_length=150)
    district = models.CharField(choices=CHOICE_DISTRICT, max_length=70)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('T', 'T-Shart'),
    ('J', 'Jeans'),
    ('MS', 'Shoes'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
    ('B', 'Bra'),
    ('LS', 'Shoes'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICE = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price