'''
Created on May 24, 2016

@author: pete
'''

# This script uses the breather class to estimate the breathing rate from
# experiments performed with the EVB1000s.
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, '../my_span_package') # Adds higher directory to python modules path.
import cir_class as cir

fname = 'data/2016_05_10/test_12bpm.txt'

my_breather = cir.breather(N_up=8,adj_type='pl',fname=fname,fs=None,win_len=30)

br_rate_vec = []
timestamp_vec = []

with open(fname,'r') as f:
    for line in f:
        
        my_breather.new_measurement(line)
        
        br_rate_vec.append(my_breather.get_br_est())
        timestamp_vec.append(my_breather.get_rel_time())

br_rate_vec = np.array(br_rate_vec)*60
timestamp_vec = np.array(timestamp_vec)

plt.plot(timestamp_vec,br_rate_vec)
plt.show()
        
    