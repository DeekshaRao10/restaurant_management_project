from django.db import models
class OrderStatus(models.Model):
    name=models.CharField(max_length=50)
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

