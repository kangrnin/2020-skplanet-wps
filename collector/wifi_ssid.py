import subprocess
import time
import datetime

subprocess.run(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=disabled'])
subprocess.run(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=enabled'])

time.sleep(3)
output = subprocess.run(
    ["netsh", "wlan", "show", "network", "mode=Bssid"],
    capture_output=True, text=True).stdout

results = output.split('\n\n')[1:-1]

timestamp = datetime.datetime.now()
wifis = []
for result in results:
    lines = result.split('\n')
    ssid = lines[0].split()[-1]
    # BSSID가 여러 개 있으면 맨 처음것만 가져옴
    signal = lines[5].split()[-1]
    wifis.append({'ssid':ssid, 'signal':signal, 'timestamp':timestamp})

print(*wifis, sep='\n')