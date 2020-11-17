import subprocess
import time
import datetime

def get_wifis():
    subprocess.run(
        ['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=disabled'],
        capture_output=True)
    subprocess.run(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=enabled'],
        capture_output=True)

    time.sleep(3)
    output = subprocess.run(
        ['netsh', 'wlan', 'show', 'network', 'mode=Bssid'],
        capture_output=True, text=True, encoding='ISO-8859-1').stdout

    results = output.split('\n\n')[1:-1]

    timestamp = datetime.datetime.now()
    wifis = []
    for result in results:
        lines = result.split('\n')

        for i in range(len(lines)):
            if lines[i].split()[0] == 'BSSID':
                bssid = lines[i].split()[-1]
                signal = lines[i+1].split()[-1][:-1]
                wifis.append({'bssid':bssid, 'signal':signal, 'timestamp':timestamp})

    return wifis

def enable_wifi():
    subprocess.run(
        ['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=enabled'],
        capture_output=True)

if __name__ == "__main__":
    wifis = get_wifis()
    print(*wifis, sep='\n')