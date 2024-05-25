from django.contrib.auth.models import User
from django.db import models

from common.models import BaseModel


class ShoppingList(BaseModel):
    name = models.CharField(max_length=200)
    items = models.ManyToManyField('ShoppingItem', related_name='shopping_lists')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.
class ShoppingItem(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.name
