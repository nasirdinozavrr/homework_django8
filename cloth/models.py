from django.db import models

class CustomerCL(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class TagCL(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductCL(models.Model):
    COLOR = (
        ("white", "white"),
        ("yellow", "yellow"),
        ("orange", "orange"),
        ("red", "red"),
        ("pink", "pink"),
        ("brown", "brown"),
        ("purple", "purple"),
        ("green", "green"),
        ("blue", "blue"),
        ("grey", "grey"),
        ("black", "black"),
    )

    SEX = (
        ("Men", "Men"),
        ("Women", "Women"),
        ("Unisex", "Unisex"),

    )
    SIZE = (
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    )

    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежда"

    name = models.CharField(max_length=200)
    color = models.CharField(choices=COLOR, max_length=100)
    size = models.CharField(choices=SIZE, max_length=100)
    sex = models.CharField(choices=SEX, max_length=100)
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name

class OrderCL(models.Model):
    STATUS = (
        ("Обробатывается", "Обробатывается"),
        ("Выехал", "Выехал"),
        ("Доставлен", "Доставлен"),
    )
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(
        ProductCL, on_delete=models.CASCADE, related_name="order_product"
    )
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.product.clothes










