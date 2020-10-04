import subprocess
import time

subprocess.run(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=disabled'])
subprocess.run(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=enabled'])

time.sleep(3)
output = subprocess.run(
    ["netsh", "wlan", "show", "network", "mode=Bssid"],
    capture_output=True, text=True).stdout

print(output)