from os import listdir
from os.path import isfile, join

def filter_by_signal():
    datafiles = [f for f in listdir('../signal_data')]
    for filename in datafiles:
        # with open('../signal_data/'+filename, 'r') as fr:
        with open('../test/signal_data/'+filename, 'r') as fr:
            filtered = []
            for line in [l for l in fr.read().split('\n') if len(l)>0]:
                # received signal strength > 40%
                if int(line.split(',')[1][:-1]) >= 40:
                    filtered.append(line)

            # with open('../signal_data_filtered/'+filename, 'w+') as fw:
            with open('../test/signal_data_filtered/'+filename, 'w+') as fw:
                fw.write('\n'.join(filtered))
                
if __name__ == '__main__':
    filter_by_signal()