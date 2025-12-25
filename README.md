# Linux System Monitor (CLI)

This project is a simple command-line Linux system monitoring tool built in Python.
It demonstrates core operating system concepts such as CPU usage calculation,
memory management, disk utilization, and process inspection using the `/proc` filesystem.

The goal of this project is to showcase practical systems programming skills and
an understanding of how operating system metrics are collected and analyzed.

---

## Features
- CPU usage percentage calculation
- Memory usage monitoring
- Disk usage monitoring for a given path
- Top processes by memory usage (RSS)
- Command-line arguments for customization

---

## Project Structure
- `monitor.py` — Main entry point for the system monitor
- `cpu.py` — CPU usage reading and calculation
- `memory.py` — Memory usage reader
- `disk.py` — Disk usage reader
- `processes.py` — Process inspection utilities
- `cli.py` — Command-line argument parsing
- `utils.py` — Helper and formatting utilities

---

## Technologies
- Python 3
- Linux (`/proc` filesystem)
- Standard Python libraries only

---

## How It Works (Overview)
- CPU usage is calculated by sampling `/proc/stat` over a short interval
- Memory usage is read from `/proc/meminfo`
- Disk usage is retrieved using Python’s `shutil.disk_usage`
- Process information is collected from `/proc/[pid]/`

---

## Usage Examples

Run with default settings:
```bash
python3 monitor.py
