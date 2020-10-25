import os
from pathlib import Path

def filter_by_signal():
    script_path = Path(__file__).parent
    raw_path = (script_path / '../signal_data/raw').resolve()
    filtered_path = (script_path / '../signal_data/filtered').resolve()

    for data_path in raw_path.glob('**/*'):
        with open(data_path, 'r') as fr:
            filtered = []
            for line in [l for l in fr.read().split('\n') if len(l)>0]:
                # received signal strength > 40%
                if int(line.split(',')[1][:-1]) >= 40:
                    filtered.append(line)

            with open(filtered_path / data_path.name, 'w+') as fw:
                fw.write('\n'.join(filtered))
                
if __name__ == '__main__':
    filter_by_signal()