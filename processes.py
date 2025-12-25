import os


def list_pids():
    return [pid for pid in os.listdir("/proc") if pid.isdigit()]


def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except (FileNotFoundError, PermissionError):
        return None


def get_process_name(pid):
    data = read_file(f"/proc/{pid}/comm")
    if not data:
        return None
    return data.strip()


def get_process_memory_kb(pid):
    """
    Returns RSS (resident set size) in KB, approximated from /proc/[pid]/status.
    """
    status = read_file(f"/proc/{pid}/status")
    if not status:
        return None

    for line in status.splitlines():
        if line.startswith("VmRSS:"):
            parts = line.split()
            if len(parts) >= 2:
                return int(parts[1])  # KB
    return None


def get_top_processes_by_memory(limit=5):
    processes = []
    for pid in list_pids():
        name = get_process_name(pid)
        mem_kb = get_process_memory_kb(pid)
        if name and mem_kb is not None:
            processes.append((pid, name, mem_kb))

    processes.sort(key=lambda x: x[2], reverse=True)
    return processes[:limit]
