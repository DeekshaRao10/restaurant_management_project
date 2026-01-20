from datetime import datetime
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