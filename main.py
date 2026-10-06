import socket
import psutil

print("Nome:", socket.gethostname())
print("CPU:", psutil.cpu_percent(interval=1), "%")
print("Memória:", psutil.virtual_memory().percent, "%")
print("Disco:", psutil.disk_usage("/").percent, "%")