import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from wifi_scan_bssid import get_wifis
from collections import defaultdict

model = joblib.load('../ml_data/model_randomforest.plk')
wifi_df = joblib.load('../ml_data/input_dataframe.plk')

while True:
    wifis = get_wifis()

    wifi_dict = defaultdict.fromkeys(wifi_df.columns, 0)
    for wifi in wifis:
        if wifi['bssid'] in wifi_dict:
            wifi_dict[wifi['bssid']] = int(wifi['signal'][:-1])


    wifi_df = wifi_df.append(pd.DataFrame.from_dict([wifi_dict]))
    print('current location : '+str(model.predict(wifi_df.tail(1))[0]))