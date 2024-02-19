
from datetime import datetime, timedelta

def subtract_five_days_from_current_date():
    current_date = datetime.now()
    
    new_date = current_date - timedelta(days=5)
    return new_date

def main():
    result_date = subtract_five_days_from_current_date()
    print("Date five days ago:", result_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    main()