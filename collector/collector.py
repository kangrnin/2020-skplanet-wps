import pandas as pd
from wifi_bssid import get_wifis, enable_wifi

def collect(rp, cnt):
    wifis = []
    for i in range(cnt):
        wifis += get_wifis()
        print('completed scan #'+str(i+1))
    
    df = pd.DataFrame(wifis)
    #df.to_csv('../signal_data/rp_'+str(rp)+'.csv', mode='a', index=False, header=False)
    df.to_csv('../test/signal_data/rp_'+str(rp)+'.csv', mode='a', index=False, header=False)

if __name__ == "__main__":
    while True:
        rp = int(input('Enter RP : '))
        if rp == -1:
            break
        cnt = int(input('Enter # of scans : '))
        collect(rp, cnt)
        
        