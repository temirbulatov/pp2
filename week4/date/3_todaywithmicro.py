from datetime import datetime

def drop_microseconds(dt):
    dt_without_microseconds = dt.strftime("%Y-%m-%d %H:%M:%S")
    dt_without_microseconds = datetime.strptime(dt_without_microseconds, "%Y-%m-%d %H:%M:%S")
    return dt_without_microseconds

current_datetime = datetime.now()

print("Original datetime:", current_datetime)
