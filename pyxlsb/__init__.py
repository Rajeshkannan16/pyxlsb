from .workbook import Workbook
from .xlsbpackage import XlsbPackage

def open_workbook(name, *args, **kwargs):
    return Workbook(XlsbPackage(name), *args, **kwargs)

def convert_date(date):
    if not isinstance(date, int) and not isinstance(date, float):
        return None

    from datetime import datetime, timedelta
    if int(date) == 0:
        return datetime(1900, 1, 1, 0, 0, 0) + timedelta(seconds=date * 24 * 60 * 60)
    elif date >= 61:
        # According to Lotus 1-2-3, Feb 29th 1900 is a real thing, therefore we have to remove one day after that date
        return datetime(1899, 12, 31, 0, 0, 0) + timedelta(days=int(date) - 1, seconds=int((date % 1) * 24 * 60 * 60))
    else:
        # Feb 29th 1900 will show up as Mar 1st 1900 because Python won't handle that date
        return datetime(1899, 12, 31, 0, 0, 0) + timedelta(days=int(date), seconds=int((date % 1) * 24 * 60 * 60))
