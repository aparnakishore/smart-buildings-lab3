import csv
import seaborn as sn
import matplotlib.pyplot as plt
from pylab import savefig
import matplotlib.image as mpimg 
from matplotlib.colors import LogNorm
import math

#with open("../try.csv", 'r') as f:
#    wines = list(csv.reader(f, delimiter=";"))
import numpy as np

save_path = "/Users/aparnak/Desktop/"
wines = np.genfromtxt('data_heatmap.csv',skip_header=1,delimiter=',',usecols=[1])
arr_2d = np.reshape(wines, (10, 20))
arr_2d[arr_2d == 0] = 1
print(arr_2d)
# setting the parameter values
#annot = True
# setting the parameter values
linewidths = 0.5
linecolor = "yellow"

#Taking log
log_norm = LogNorm(vmin=arr_2d.min().min(), vmax=arr_2d.max().max())
cbar_ticks = [math.pow(10, i) for i in range(math.floor(math.log10(arr_2d.min().min())), 1+math.ceil(math.log10(arr_2d.max().max())))]


# setting the parameter values
xticklabels = False
yticklabels = False
cmap = "plasma"
# setting the parameter values
# plotting the heatmap
hm = sn.heatmap(data = arr_2d, cmap = cmap,linewidths=linewidths,linecolor=linecolor, alpha=0.5, zorder = 2, norm=log_norm, cbar_kws={"ticks": cbar_ticks}, xticklabels=xticklabels,
                yticklabels=yticklabels)
#plt.show()

#figure = hm.get_figure()
#figure.savefig(save_path+'lab_heatmap.png', dpi=400)
map_img = mpimg.imread('lll_grid.png')

hm.imshow(map_img,
          aspect = hm.get_aspect(),
          extent = hm.get_xlim() + hm.get_ylim(),
          zorder = 1) #put the map under the heatmap

#plt.figure(figsize = (10,10))
#plt.imshow(hm)
#plt.imshow(map_img, alpha=0.5)
#from matplotlib.spyplot import show 
plt.show()
figure = hm.get_figure()
figure.savefig(save_path+'lab_heatmap.png', dpi=600)