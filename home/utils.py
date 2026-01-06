from datetime import datetime
from .models import DailyOperatingHours
def get_today_operating_hours():
    today=datetime.now().strftime('%A')
    try:
        operating_hours=DailyOperatingHours.get(day=today)
        return operating_hours.open_time,operating_hours.close_time
    except DailyOperatingHours.DoesNotExist:
        return None, None