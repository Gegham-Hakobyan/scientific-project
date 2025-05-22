import psutil
import time
import matplotlib.pyplot as plt
from threading import Thread
import compute

cpu_usage = []
mem_usage = []
time_points = []

def monitor(interval=0.5, duration=10):
    for i in range(int(duration / interval)):
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        cpu_usage.append(cpu)
        mem_usage.append(mem)
        time_points.append(i * interval)
        time.sleep(interval)

if __name__ == "__main__":
    monitor_thread = Thread(target=monitor)
    monitor_thread.start()

    compute.heavy_compute()

    monitor_thread.join()

    plt.plot(time_points, cpu_usage, label="CPU Usage (%)")
    plt.plot(time_points, mem_usage, label="Memory Usage (%)")
    plt.xlabel("Time (s)")
    plt.ylabel("Usage (%)")
    plt.title("Resource Usage During Computation")
    plt.legend()
    plt.savefig("resource_usage.png")
    print("График сохранён: resource_usage.png")

