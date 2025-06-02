copilot_test.py
This script prints your system's uptime in a human-readable format. It works on both Unix/Linux and Windows systems.

What does it do?
On Unix/Linux: Reads the system uptime from /proc/uptime and displays the time in hours, minutes, and seconds.
On Windows: Uses the net stats srv command to print the system uptime since the last boot.
If the operating system is not supported, it will display an "Unsupported OS" message.
How to run
Make sure you have Python installed (compatible with Python 3).
Download or clone this repository.
Open a terminal (or command prompt) and navigate to the directory containing copilot_test.py.
Run the script with the following command:
Code
python copilot_test.py
You will see an output displaying your system's uptime.
