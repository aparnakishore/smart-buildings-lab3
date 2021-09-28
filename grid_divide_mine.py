import pickle
import json
import utility as util
import pandas as pd
import utility as util
from datetime import datetime
import seaborn as sns # imports the seaborn module (https://seaborn.pydata.org/)
import matplotlib.pyplot as plt # imports the python data visualization library object (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)


def main():
    # divide into grids
    d = {}
    grid_size = 3.05
    count = -1

    with open('book.pickle', 'rb') as f:
        df = pickle.load(f)

    for y in range(0, 10):
        y_cor = grid_size * (10 - y)
        # print('X cor: %.2f' % x_cor)
        # Get all the x related values
        ydf = df[(df['y'] < y_cor) & (df['y'] > (y_cor - grid_size))]
        for x in range(0, 20):
            x_cor = x * grid_size
            xdf = ydf[(ydf['x'] > (x_cor - grid_size))
                      & (ydf['x'] < x_cor)].copy()
            # print('(%.2f, %.2f)' % (x_cor, y_cor), end='\t')
            print(count, end='\t')
            if not xdf.empty:
                # dict['[%s] %.2f, %.2f' % (count, x_cor, y_cor)] = xdf
                d[count] = xdf
            count += 1
       # print()
    return d

# if loc.x < x and loc.y < y


if __name__ == '__main__':
    d = main()
   # for key in d:
      #  print('%s: ' % key)
      #  print(d[key])
      #  print('-' * 80)

   # print(d)
    # output.json = json.dumps(d)

#find which sensors are at the grid I'm interested in
    # file_to_write.close()
    with open('test.pickle','wb') as f:
        pickle.dump(d, f)
    
    with open('test.pickle','rb') as f:
        d = pickle.load(f)
    
  #  print(d)

#data for that sensor for a specific time range
s= datetime(2021,1,1) # start datetime
e= datetime(2021,9,20) # end datetime
fields = list(set(d[2]['fields'].values[0].split(',')))
#print(fields)
# ['Illumination_lx', 'rssi', 'Supply voltage_V', 'Range select']
df = util.get_lfdf('Illumination_lx', s, e, list(d[2]['device_id']))

#print (df)

#For plotting
#sns.lineplot(x= 'time', y='value', data=df)
#plt.title('Lux Value Over Time')
#plt.show() # Shows the plot