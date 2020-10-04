import pandas as pd
from wifi_bssid import get_wifis, enable_wifi

def collect(rp):
    wifis = []
    cnt = 0
    while True:
        try:
            wifis += get_wifis()
            print('completed scan #'+cnt)
            cnt += 1
            
        except KeyboardInterrupt:
            enable_wifi()
            break
    
    df = pd.DataFrame(wifis)
    df.to_csv('../signal_data/rp_'+str(rp)+'.csv', mode='a', index=False, header=False)

if __name__ == "__main__":
    while (rp := int(input('Enter RP (-1 = exit) : '))) != -1:
        collect(rp)
        
        