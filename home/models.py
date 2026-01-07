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