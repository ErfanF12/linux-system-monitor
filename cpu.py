import time


def read_cpu_times():
    """
    Reads CPU time stats from /proc/stat
    Returns (total_time, idle_time)
    """
    with open("/proc/stat", "r") as file:
        cpu_line = file.readline()

    values = cpu_line.split()[1:]
    values = [int(v) for v in values]

    total = sum(values)
    idle = values[3]
    return total, idle


def get_cpu_usage_percent(interval=1):
    """
    Calculates CPU usage percentage over a short interval.
    """
    total1, idle1 = read_cpu_times()
    time.sleep(interval)
    total2, idle2 = read_cpu_times()

    total_delta = total2 - total1
    idle_delta = idle2 - idle1

    if total_delta == 0:
        return 0.0

    usage = 100.0 * (1.0 - (idle_delta / total_delta))
    return round(usage, 2)
