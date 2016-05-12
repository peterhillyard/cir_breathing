# This script plots the CIR pdp and the power over time. This script is intended
# for plotting the results of the 2016_05_06 experiments where I did the 
# on, off, and nearby the link line experiments. These experiments only consider
# a link in one location. Only the environment changed.
import numpy as np
import cir_class_master as cir
import matplotlib.pyplot as plt
import os

# Parameters
fname = 'test_13bpm.txt'
my_cir_obj = cir.cir_power_class(N_up=8,adj_type='pl',sig_type='m')
power_vec = []
pdp_mat = []
time_vec = []

with open('data/2016_05_10/' + fname,'r') as f:
    for line in f:
        
        if my_cir_obj.observe(line) == 0:
            continue
        
        power_vec.append(my_cir_obj.get_full_power())
        pdp_mat.append(my_cir_obj.get_cir_mag().tolist())
        time_vec.append(my_cir_obj.get_rel_time())

power_vec = np.array(power_vec)
pdp_mat = np.array(pdp_mat).T
time_vec = np.array(time_vec)

y_max = my_cir_obj.num_taps
xing_y_val = my_cir_obj.first_path_tap_idx

if os.path.isfile('data/xings/' + fname):
    xings = np.loadtxt('data/xings/' + fname)
else:
    xings = None

plt.subplot(2,1,1)
plt.imshow(pdp_mat,origin='upper',aspect='auto',interpolation='none',
           extent = (time_vec[0],time_vec[-1],y_max,0))
if xings is not None:
    plt.plot(xings,xing_y_val*np.ones(xings.size),'rx',ms=10,mew=10)
plt.xlim(time_vec[0],time_vec[-1])
plt.xlabel('Time (sec)')
plt.ylabel('Time delay (ns)')
plt.subplot(2,1,2)
plt.plot(time_vec,power_vec)
if xings is not None:
    plt.plot(xings,np.median(power_vec)*np.ones(xings.size),'rx',ms=10,mew=10)
plt.xlim(time_vec[0],time_vec[-1])
plt.xlabel('Time (sec)')
plt.ylabel('Power (dB)')
plt.show()









