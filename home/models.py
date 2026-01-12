from django.db import models
class Restaurant(models.Model):
    name=models.CharField(max_length=255)
    owner_name=models.CharField(max_length=255)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    address=models.TextField()
    city=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_(default=False)
    def __str__(self):
        return self.name
class DailySpecial(models.Model):
    restaurant=models.ForiegnKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='daily_specials'
    )
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits,decimal_places=2)
    created_at=models.DateTimeField(aauto_now_add=True)
    def __str__(self):
        return self.name
    @staticmethod
    def get_random_special():
        specials=DailySpecial.objects.all()
        if specials.exists():
            return specials.order_by('?').first()
        return None
