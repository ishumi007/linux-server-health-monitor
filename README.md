# Linux Server Health Monitor

## Overview
Linux Server Health Monitor is a Python-based monitoring tool designed to track
the real-time health of a Linux server. It helps identify potential issues such
as high CPU usage, memory exhaustion, disk space shortages, and stopped system
services before they cause downtime.

This project demonstrates practical DevOps fundamentals commonly used in
production environments, including system monitoring, automation, and
infrastructure reliability.

---

## Why This Project
In real-world systems, most outages happen due to:
- Resource exhaustion (CPU, memory, disk)
- Unmonitored service failures
- Lack of visibility into system health

This tool provides a simple but effective way to monitor these risks and act
early.

---

## Features
- CPU usage monitoring
- Memory utilization tracking
- Disk usage monitoring
- Linux service health checks
- Threshold-based warnings
- Timestamped logging for auditing and debugging

---

## Tech Stack
- Python 3
- Linux
- psutil (system and process utilities)
- Git & GitHub

---

## How It Works
The script collects live system metrics using the psutil library. Each metric is
evaluated against predefined thresholds. If usage exceeds limits or a service is
not running, a warning is generated and logged with a timestamp.

---


## Setup (Recommended)

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
# venv\Scripts\activate    # Windows
```

## How to Run
```bash
pip install -r requirements.txt
python3 monitor.py
```

## Author
Ishu Mishra  
DevOps & Infrastructure Enthusiast 

## License
MIT

## Future Improvements
- Docker support
- Cron-based scheduling
- Alerting via email/Slack
