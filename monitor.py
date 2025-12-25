from cpu import get_cpu_usage_percent
from memory import get_memory_usage
from disk import get_disk_usage
from utils import kb_to_gb, bytes_to_gb, format_percent


def main():
    print("=== Linux System Monitor ===")

    cpu_percent = get_cpu_usage_percent(interval=1)

    mem_total_kb, mem_free_kb = get_memory_usage()
    mem_used_kb = mem_total_kb - mem_free_kb

    disk_total_b, disk_used_b, disk_free_b = get_disk_usage("/")

    print(f"CPU Usage: {format_percent(cpu_percent)}")
    print(
        f"Memory: {kb_to_gb(mem_used_kb)} GB used / {kb_to_gb(mem_total_kb)} GB total"
    )
    print(
        f"Disk (/): {bytes_to_gb(disk_used_b)} GB used / {bytes_to_gb(disk_total_b)} GB total"
    )


if __name__ == "__main__":
    main()
