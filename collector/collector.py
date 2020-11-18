from pathlib import Path
import pandas as pd
from wifi_scan import get_wifis, enable_wifi

def collect(position, rp, cnt):
    #position = str(position)

    script_path = Path(__file__).parent
    data_path = script_path / '../signal_data'
    # 데이터 파일 폴더 생성
    data_path.mkdir(parents=True, exist_ok=True)
    (data_path/position).mkdir(parents=True, exist_ok=True)

    wifis = []
    for i in range(cnt):
        wifis += get_wifis()
        print('completed scan #'+str(i+1))
    
    # (position) 폴더 안의 (rp).csv 안에 저장
    df = pd.DataFrame(wifis)
    df.to_csv(data_path/position/(rp+'.csv'), mode='a', index=False, header=False)

    # position, rp 정보 column을 추가해서 통합 데이터파일에도 저장
    df['position'] = position
    df['rp'] = rp
    df.to_csv(data_path/'signal_all.csv', mode='a', index=False, header=False)

if __name__ == "__main__":
    while True:
        position = input('Enter Position : ')
        rp = input('Enter RP : ')
        cnt = int(input('Enter # of scans : '))
        collect(position, rp, cnt)
        
        