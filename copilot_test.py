import os

def print_system_uptime():
    # Works on Unix/Linux systems
    if os.name == 'posix':
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            hours = int(uptime_seconds // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            seconds = int(uptime_seconds % 60)
            print(f"System uptime: {hours}h {minutes}m {seconds}s")
    # Works on Windows systems
    elif os.name == 'nt':
        import subprocess
        output = subprocess.check_output("net stats srv", shell=True, text=True)
        for line in output.splitlines():
            if "Statistics since" in line:
                print("System uptime (since):", line)
                break
    else:
        print("Unsupported OS")

if __name__ == "__main__":
    print_system_uptime()
