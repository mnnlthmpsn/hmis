from django.db import models
from staffAuth.models import Staff

# Create your models here.
class Logs(models.Model):
    period = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=200)

    def __repr__(self):
        return self.period

class Drug(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Unit Price')
    qty_in_stock = models.PositiveIntegerField(verbose_name='Quantity Available', default=0)

    def __str__(self):
        return self.name

class Sales(models.Model):
    period = models.DateField(auto_now_add=True)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Selling Price')
    seller = models.ForeignKey(Staff, on_delete=models.CASCADE)
    qty_sold = models.IntegerField(verbose_name='Quantity Sold')

    def __unicode__(self):
        return u"from UTC:{0}".format(self.period)