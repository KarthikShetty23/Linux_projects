import psutil
import datetime
import socket

def check_network():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return "Online"
    except OSError:
        return "Offline"

def log_system_health():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network_status = check_network()

    alert = ""
    if cpu_usage > 80.0:
        alert += "[WARNING: High CPU] "
    if ram_usage > 85.0:
        alert += "[WARNING: High RAM] "

    log_entry = f"[{timestamp}] CPU: {cpu_usage}% | RAM: {ram_usage}% | Disk: {disk_usage}% | Net: {network_status} | {alert}\n"

    with open("system_health.log", "a") as log_file:
        log_file.write(log_entry)

    print(f"Health check saved: {log_entry.strip()}")

if __name__ == "__main__":
    log_system_health()


    # this program is about checking the health monitoring of the system, it looks at differnt components like CPU, RAM.and current time. 
    # if the cpu and ram more than 80% , it gives us an alert about overusage of the system.