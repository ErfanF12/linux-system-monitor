import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Linux System Monitor - CLI tool for CPU, memory, disk, and processes."
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=1,
        help="Seconds to sample CPU usage (default: 1)",
    )

    parser.add_argument(
        "--path",
        type=str,
        default="/",
        help="Disk path to monitor (default: /)",
    )

    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of top processes to show (default: 5)",
    )

    return parser.parse_args()
