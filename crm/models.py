from django.db import models


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200)
    order_phone = models.CharField(max_length=200)
