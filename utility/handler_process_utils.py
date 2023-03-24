import pytz
from datetime import datetime

def handle_error(msg):
    print("ERROR: ", msg)

def raise_error(msg):
    raise Exception(msg)

def datetime_utc_now_CRM():
    time_zone = pytz.timezone('America/Bogota')
    dt = datetime.now(time_zone)
    dt = dt.strftime('%Y-%m-%d %H:%M:%S')
    return str(dt).replace(' ', 'T')