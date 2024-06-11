import psutil

# Define thresholds
cpu_threshold = 80  # in percentage
memory_threshold = 80  # in percentage
disk_threshold = 80  # in percentage

# Function to check CPU usage
def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > cpu_threshold:
        print(f"Alert: CPU usage is {cpu_percent}% (Threshold: {cpu_threshold}%)")

# Function to check memory usage
def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > memory_threshold:
        print(f"Alert: Memory usage is {memory_percent}% (Threshold: {memory_threshold}%)")

# Function to check disk usage
def check_disk_usage():
    disk_percent = psutil.disk_usage('/').percent
    if disk_percent > disk_threshold:
        print(f"Alert: Disk usage is {disk_percent}% (Threshold: {disk_threshold}%)")

# Function to check running processes
def check_running_processes():
    num_processes = len(psutil.pids())
    print(f"Number of running processes: {num_processes}")

# Main function
def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()
