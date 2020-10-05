from collections import defaultdict

def count_bssid(start, end):
    rp_set = set()
    for i in range(start, end+1):
        with open('../signal_data/rp_'+str(i)+'.csv', 'r') as file:
            scans = defaultdict(list)
            for line in [l for l in file.read().split('\n') if len(l) != 0]:
                bssid = line.split(',')[0]
                signal = line.split(',')[1]
                timestamp = line.split(',')[2]
                scans[timestamp] += {'bssid':bssid, 'signal':signal}

            for wifi_list in scans:
                wifi_list.sort(key=lambda x: x[signal])

            # TODO : 
            # 정렬해서 top 몇개가 아니라 신호가 특정 수치 이하인 것들을 제외하자


    rp_set = sorted(rp_set)
    print(rp_set)
    print(len(rp_set), sep='\n')
                
if __name__ == "__main__":
    count_bssid(*[int(i) for i in input('start, end : ').split()])