from django.db import models


class Product(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    created_at = models.DateField()
    image = models.ImageField(upload_to="shop/images",
                              default="")

    def __str__(self):
        return self.name
