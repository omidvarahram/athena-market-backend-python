from datetime import datetime

def convert_date_time_to_iso_timestamp(date_string, time_string):
    datetime_string = f"{date_string} {time_string}"
    timestamp = datetime.strptime(datetime_string, "%Y.%m.%d %H:%M")
    return timestamp.isoformat()