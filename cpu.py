def get_cpu_usage():
    """
    Reads CPU usage information from /proc/stat
    """
    with open("/proc/stat", "r") as file:
        lines = file.readlines()

    cpu_line = lines[0]
    values = cpu_line.split()[1:]
    values = [int(v) for v in values]

    total = sum(values)
    idle = values[3]

    return total, idle
