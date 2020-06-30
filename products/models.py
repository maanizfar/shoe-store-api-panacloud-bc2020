from django.db import models


class Product(models.Model):

    gender_choices = [
        ('M', 'Men'),
        ('F', 'Women'),
        ('K', 'Kids')
    ]

    category_choices = [
        ('RUNNING', 'Running'),
        ('FOOTBALL', 'Football'),
        ('CASUAL', 'Casual'),
        ('FORMAL', 'Formal'),
    ]

    brands = [
        ('NIKE', 'Nike'),
        ('ADIDAS', 'Adidas')
    ]

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=20, choices=brands, default='NIKE')
    main_category = models.CharField(
        max_length=1, choices=gender_choices,)
    sub_category = models.CharField(
        max_length=10, choices=category_choices,)
    price = models.PositiveIntegerField()
    imageURL = models.URLField()
    is_in_inventory = models.BooleanField(default=True)

    def __str__(self):
        return self.name
