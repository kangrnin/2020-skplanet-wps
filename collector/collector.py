from pathlib import Path
import pandas as pd
from wifi_bssid import get_wifis, enable_wifi

def collect(rp, cnt):
    script_path = Path(__file__).parent
    raw_path = script_path / '../signal_data/raw'
    raw_path.mkdir(parents=True, exist_ok=True)

    wifis = []
    for i in range(cnt):
        wifis += get_wifis()
        print('completed scan #'+str(i+1))
    
    df = pd.DataFrame(wifis)
    df.to_csv(raw_path/('rp_'+rp+'.csv'), mode='a', index=False, header=False)

if __name__ == "__main__":
    while True:
        rp = input('Enter RP : ')
        cnt = int(input('Enter # of scans : '))
        collect(rp, cnt)
        
        