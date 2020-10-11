from os import listdir
from os.path import isfile, join

def count_bssid():
    datafiles = [f for f in listdir('../signal_data_filtered')]
    total_set = set()
    for filename in datafiles:
        with open('../signal_data_filtered/'+filename, 'r') as fr:
            bssid_set = set()
            for line in [l for l in fr.read().split('\n') if len(l)>0]:
                bssid_set.add(line.split(',')[0])
                total_set.add(line.split(',')[0])
            print('distinct bssids in '+filename+' : '+str(len(bssid_set)))
    print('total distinct bssids : '+str(len(total_set)))

if __name__ == '__main__':
    count_bssid()