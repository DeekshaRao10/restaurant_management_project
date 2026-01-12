import secrets
import string
from .models import Coupon
def generate_coupon_code(length=10):
    characters=string.ascii_uppercase+string.digits
    while True:
        code=''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code
def get_daily_sales_total(Data):
    result=Order.objects.filter(
        created_at__date=created_at__date
    ).aggregate(total_sum=sum('total_price'))
    return result['total_sum'] or 0