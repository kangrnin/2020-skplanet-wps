import subprocess
import time

def get_wifis():
    subprocess.run(
        ['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=disabled'],
        capture_output=True)
    subprocess.run(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=enabled'],
        capture_output=True)

    time.sleep(3)
    output = subprocess.run(
        ["netsh", "wlan", "show", "network", "mode=Bssid"],
        capture_output=True, text=True).stdout

    results = output.split('\n\n')[1:-1]

    wifis = []
    for result in results:
        lines = result.split('\n')
        for i in range(4, len(lines), 6):
            bssid = lines[i].split()[-1]
            signal = lines[i+1].split()[-1]
            wifis.append({'bssid':bssid, 'signal':signal})
    
    return wifis

def enable_wifi():
    subprocess.run(
        ['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=enabled'],
        capture_output=True)

if __name__ == "__main__":
    wifis = get_wifis()
    print(*wifis, sep='\n')