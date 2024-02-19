from datetime import datetime, timedelta

def get_yesterday_today_tomorrow():
    current_date = datetime.now()
    yesterday = current_date - timedelta(days=1)
    tomorrow = current_date + timedelta(days=1)
    return yesterday, current_date, tomorrow

yesterday, today, tomorrow = get_yesterday_today_tomorrow()

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))

print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))