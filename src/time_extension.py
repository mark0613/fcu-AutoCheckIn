import datetime

def time_compare(t1: str, t2: str, t_format: str) -> bool:
    """
    return whether t1 >= t2
    """
    return datetime.datetime.strptime(t1, t_format) >= datetime.datetime.strptime(t2, t_format)

def time_delta(t1: str, t2: str, t_format: str) -> int:
    """
    return abs(t2-t1)  (unit: seconds)
    """
    return (datetime.datetime.strptime(t2, t_format) - datetime.datetime.strptime(t1, t_format)).seconds
    