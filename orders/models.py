from django.db import models
from django.utils import timezone
class OrderStatus(models.Model):
    name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name
class order(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True
    )
    def __str__(self):
        return f"Order {self.id}"

class coupon(models.Model):
    code=models.CharFiels(max_length=50,unique=True)
    discount_percentage=models.DecimalField(max_digits=5,decimal_places=2)
    is_active=models.BooleanField(default=True)
    valid_from=models.DateField()
    valid_until=models.DateField()
    def __str__(self):
        return self.code
    def is_valid(self):
        today=timezone.now().date()
        return(
            self.is_active and 
            self. valid_from<=today<=self.valid_until
        )

