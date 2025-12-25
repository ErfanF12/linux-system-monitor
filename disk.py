import shutil


def get_disk_usage(path="/"):
    """
    Returns disk usage statistics
    """
    usage = shutil.disk_usage(path)
    return usage.total, usage.used, usage.free
