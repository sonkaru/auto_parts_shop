from django.db import models

class Order(models.Model):

    price = models.IntegerField()
    product = models.ForeignKey(to='product.Product', null=True, on_delete=models.SET_NULL)
    buyer = models.ForeignKey(to='user.User', null=True, on_delete=models.SET_NULL, related_name='buyer')

    def __str__(self):
        return f'{self.id} - {self.price}₸'
    
    class Meta:
        db_table = 'order'
        verbose_name = '订单'
        verbose_name_plural = '订单'