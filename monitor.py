from cpu import get_cpu_usage_percent
from memory import get_memory_usage
from disk import get_disk_usage
from utils import kb_to_gb, bytes_to_gb, format_percent
from processes import get_top_processes_by_memory
from cli import parse_args


def main():
    args = parse_args()

    print("=== Linux System Monitor ===")

    cpu_percent = get_cpu_usage_percent(interval=args.interval)

    mem_total_kb, mem_free_kb = get_memory_usage()
    mem_used_kb = mem_total_kb - mem_free_kb

    disk_total_b, disk_used_b, disk_free_b = get_disk_usage(args.path)

    print(f"CPU Usage: {format_percent(cpu_percent)}")
    print(f"Memory: {kb_to_gb(mem_used_kb)} GB used / {kb_to_gb(mem_total_kb)} GB total")
    print(
        f"Disk ({args.path}): {bytes_to_gb(disk_used_b)} GB used / {bytes_to_gb(disk_total_b)} GB total"
    )

    print("\nTop Processes by Memory (RSS):")
    top = get_top_processes_by_memory(limit=args.top)
    for pid, name, mem_kb in top:
        print(f"- PID {pid} | {name} | {kb_to_gb(mem_kb)} GB")


if __name__ == "__main__":
    main()
