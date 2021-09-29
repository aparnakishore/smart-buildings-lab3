import utility as util
import pandas as pd
import utility as util
from datetime import datetime
import seaborn as sn
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import csv
import numpy as np
from pylab import savefig
from matplotlib.colors import LogNorm
import math
import os

def generate_linklab_heatmap(start_datetime, end_datetime , fields, export_filepath):
    
    s = start_datetime
    e = end_datetime

    df = pd.read_csv("book_with_grids.csv")
    grid = list(set(df['grid']))
    sorted_grid = sorted(grid)
    header = ['grid', 'data_count']
    new_arr = np.array([])
    number = [i for i in range(200)]
    for num in number:
        if num in sorted_grid:
            field = fields
            num_readings = 0
            data = []
            for j in field:
                try:
                    readings = list(util.get_lfdf(j,s,e,list(df[df["grid"]==num]["device_id"]))['value'])
                    num_readings = num_readings + len(readings)
                except:
                    num_readings = num_readings         
            arr = np.array(num_readings)
            new_arr = np.append(new_arr,arr)

        else:
            arr = np.array(0)
            new_arr = np.append(new_arr,arr)

    try:
        arr_2d = np.reshape(new_arr, (10, 20))
        #To convert 0 to 1, so that we can take log scale to tackle large differences in the values
        arr_2d[arr_2d == 0] = 1
        # setting the parameter values
        cmap = "plasma"
        
        # setting the parameter values
        xticklabels = False
        yticklabels = False

        # setting the parameter values
        linewidths = 0.5
        linecolor = "yellow"

        #Taking log
        log_norm = LogNorm(vmin=arr_2d.min().min(), vmax=arr_2d.max().max())
        cbar_ticks = [math.pow(10, i) for i in range(math.floor(math.log10(arr_2d.min().min())), 1+math.ceil(math.log10(arr_2d.max().max())))]

        # plotting the heatmap
        hm = sn.heatmap(data = arr_2d, cmap = cmap,linewidths=linewidths,linecolor=linecolor, alpha=0.5, zorder = 2, norm=log_norm, cbar_kws={"ticks": cbar_ticks}, xticklabels=xticklabels,
        yticklabels=yticklabels)

        # add lll grid image behind heatmap
        map_img = mpimg.imread('lll_grid.png')
        hm.imshow(map_img,
                aspect = hm.get_aspect(),
                extent = hm.get_xlim() + hm.get_ylim(),
                zorder = 1) #put the map under the heatmap

        figure = hm.get_figure()
        # path = os.path.join(save_path,'lab_heatmap_1.png')
        figure.savefig(export_filepath, dpi=600) 
        return export_filepath
    except:
        return None
    
def main():
    # ask user for heatmap fxn arguments
    start = input("Enter a start date (ex. 2020,1,1): ")
    s = start.split(',')
    s = [int(i) for i in s]
    y = s[0]
    m = s[1]
    d = s[2]
    start = datetime(y,m,d)
    end = input("Enter an end date (ex. 2020,10,1): ")
    e = end.split(',')
    e = [int(i) for i in e]
    y = e[0]
    m = e[1]
    d = e[2]
    end = datetime(y,m,d)
    fil = input("Enter a field/s of interest (ex. Humidity_%, Temperature_°C, T-Sensor): ")
    fil = fil.split(',')
    filepath = input("Enter a desired filepath to export your heatmap (ex. C:\\Users\\John\\lll-heatmap.png): ")
    path = generate_linklab_heatmap(start, end , fil, filepath)
    print(path)

if __name__ == '__main__':
    main()
