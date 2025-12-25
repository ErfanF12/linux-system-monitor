def get_memory_usage():
    """
    Reads memory usage information from /proc/meminfo
    """
    mem_info = {}

    with open("/proc/meminfo", "r") as file:
        for line in file:
            key, value = line.split(":")
            mem_info[key] = int(value.strip().split()[0])

    total = mem_info.get("MemTotal", 0)
    free = mem_info.get("MemFree", 0)

    return total, free
