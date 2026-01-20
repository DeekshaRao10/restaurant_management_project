from datetime import datetime,time
import re
from .models import DailyOperatingHours
def get_today_operating_hours():
    today=datetime.now().strftime('%A')
    try:
        operating_hours=DailyOperatingHours.get(day=today)
        return operating_hours.open_time,operating_hours.close_time
    except DailyOperatingHours.DoesNotExist:
        return None, None
def is_restaurant_open():
    now=datetime.now()
    current_Day=now.weekday()
    current_time=now time()
    if current_day<5:
        open_time=time(9,0)
        close_time=time(22,0)
    else:
        open_time=time(10,0)
        close_time=time(23,0)
    return open_time<=current<=close_time
def is_valid_phone_number(phone: str) ->bool:
    if not phone:
        return False
    phone =phone.strip()
    pattern=r'^\+?\d{1,3}?\d(?:[- ]?\d){9,11}$'
    if not re.match(pattern,phone):
        return False
    digits=re.sub(r'\','',phone)
    return 10<len(digits)<=12