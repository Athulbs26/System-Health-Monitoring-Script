import psutil
import logging
from datetime import datetime
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage
    
def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert(f"High Memory usage detected: {memory_usage}%")
    return memory_usage
    
def check_disk_space():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        alert(f"Low Disk space detected: {disk_usage}% used")
    return disk_usage
    
def check_running_processes():
    processes = psutil.pids()
    return len(processes)
    
def alert(message):
    print(message)
    logging.info(message)
    
def monitor_system():
    cpu_usage = check_cpu_usage()
    memory_usage = check_memory_usage()
    disk_usage = check_disk_space()
    num_processes = check_running_processes()
    
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")
    print(f"Running Processes: {num_processes}")
    
if __name__ == "__main__":
    monitor_system()
