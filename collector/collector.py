from pathlib import Path
import pandas as pd
from wifi_scan import get_wifis, enable_wifi

def collect(position, rp):
    #position = str(position)

    script_path = Path(__file__).parent
    data_path = script_path / '../signal_data'
    # 데이터 파일 폴더 생성
    data_path.mkdir(parents=True, exist_ok=True)
    (data_path/position).mkdir(parents=True, exist_ok=True)

    wifi_list = []
    bssid_set = set()

    overlap_cnt = 0
    scan_cnt = 1
    while True:
        print('-----------------------------------------')

        scan_wifis = get_wifis()
        print('total bssid cnt : ', len(scan_wifis))

        new_bssids = [ w['bssid'] for w in scan_wifis if w['bssid'] not in bssid_set ]
        bssid_set.update(new_bssids)

        print(len(new_bssids), 'new bssids : [ ', end='')
        for bssid in new_bssids:
            print('~'+bssid[-8:], end=', ')
        print(' ]')

        overlap_cnt = overlap_cnt+1 if len(new_bssids) == 0 else 0
        
        if overlap_cnt == 3:
            break

        if new_bssids:
            wifi_list += scan_wifis

        print('completed scan #', scan_cnt)
        scan_cnt += 1
    
    # (position) 폴더 안의 (rp).csv 안에 저장
    df = pd.DataFrame(wifi_list)
    df.to_csv(data_path/position/(rp+'.csv'), mode='a', index=False, header=False)

    # position, rp 정보 column을 추가해서 통합 데이터파일에도 저장
    df['position'] = position
    df['rp'] = rp
    df.to_csv(data_path/position/'signal_all.csv', mode='a', index=False, header=False)

if __name__ == "__main__":
    while True:
        position = input('Enter Position : ')
        rp = input('Enter RP : ')
        collect(position, rp)
        
        