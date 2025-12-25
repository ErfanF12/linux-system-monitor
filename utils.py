def bytes_to_gb(num_bytes):
    return round(num_bytes / (1024 ** 3), 2)


def kb_to_gb(num_kb):
    return round(num_kb / (1024 ** 2), 2)


def format_percent(value):
    return f"{value:.2f}%"
