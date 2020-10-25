from os import listdir
from os.path import isfile, join
from pathlib import Path

def count_bssid(path):
    script_path = Path(__file__).parent
    path = (script_path / path).resolve()
    
    datafiles = [f for f in listdir(path)]
    total_set = set()
    for filename in datafiles:
        with open(path / filename, 'r') as fr:
            bssid_set = set()
            for line in [l for l in fr.read().split('\n') if len(l)>0]:
                bssid_set.add(line.split(',')[0])
                total_set.add(line.split(',')[0])
            print('distinct bssids in '+str(filename)+' : '+str(len(bssid_set)))
    print('total distinct bssids : '+str(len(total_set)))

if __name__ == '__main__':
    print('*** raw ***')
    count_bssid('../signal_data/raw')
    print('\n*** filtered ***')
    count_bssid('../signal_data/filtered/')
