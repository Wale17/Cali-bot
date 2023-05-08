import pytz
from datetime import datetime
from robot.api import logger


def handle_error(msg):
    print("ERROR: ", msg)

def raise_error(msg):
    raise Exception(msg)

def datetime_utc_now_CRM():
    time_zone = pytz.timezone('America/Bogota')
    dt = datetime.now(time_zone)
    dt = dt.strftime('%Y-%m-%d %H:%M:%S')
    return str(dt).replace(' ', 'T')

def log_message(message: str, level: str = 'INFO', console: bool = True):
    log_switcher = {
        'TRACE': logger.trace,
        'INFO': logger.info,
        'WARN': logger.warn,
        'ERROR': logger.error
    }
    if not level.upper() in log_switcher.keys() or level.upper() == 'INFO':
        logger.info(message, True, console)
    else:
        if level.upper() == 'ERROR':
            logger.info(message, True, console)
        else:
            log_switcher.get(level.upper(), logger.error)(message, True)
