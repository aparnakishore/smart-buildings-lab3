import pickle
import json
import utility as util
import pandas as pd
import utility as util
from datetime import datetime
import seaborn as sns 
import matplotlib.pyplot as plt 
import csv

df = pd.read_csv("book_with_grids.csv")

#print(len(set(df["type"])))
s= datetime(2021,1,1) # start datetime
e= datetime(2021,9,23) # end datetime
#readings = list(util.get_lfdf("Humidity_%",s,e,list(df[df["grid"]==6]["device_id"]))['value'])
#print(len(readings))
grid = list(set(df['grid']))
sorted_grid = sorted(grid)

header = ['grid', 'data_count']

with open('data_heatmap.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    number = [i for i in range(200)]

    for num in number:
        if num in sorted_grid:
            fields = list(df[df["grid"]==num]["fields"].values[0].split(','))
            num_readings = 0
            data = []
            for j in fields:
                try:
                    readings = list(util.get_lfdf(j,s,e,list(df[df["grid"]==num]["device_id"]))['value'])
                    num_readings = num_readings + len(readings)
                except:
                    num_readings = num_readings         
            print("grid:", num, " devices:", num_readings)
            data.append(num)
            data.append(num_readings)
            writer.writerow(data)

        else:
            data = [num,0]
            writer.writerow(data)
