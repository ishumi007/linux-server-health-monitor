import psutil

cpu_usage = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')




CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

if cpu_usage > CPU_THRESHOLD:
    print("⚠️ High CPU usage!")

if memory.percent > MEM_THRESHOLD:
    print("⚠️ High Memory usage!")

if disk.percent > DISK_THRESHOLD:
    print("⚠️ High Disk usage!")


def is_service_running(service_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == service_name:
            return True
    return False

service = "ssh"

if is_service_running(service):
    print(f"Service {service} is running")
else:
    print(f"❌ Service {service} is NOT running")


from datetime import datetime

log_file = "health.log"

def log(message):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")


log(f"CPU Usage: {cpu_usage}%")
log(f"Memory Usage: {memory.percent}%")
log(f"Disk Usage: {disk.percent}%")
