import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 2
mpl.rc('xtick', labelsize=24) 
mpl.rc('ytick', labelsize=24) 
mpl.rc('axes', labelsize=24) 
mpl.rc('font', size=24)

# Load arrays from file
data = np.load("optimization_results.npz")
obj_vals_CONMIN = data['obj_vals_CONMIN']
cl_con_vals_CONMIN = data['cl_con_vals_CONMIN']
cm_con_vals_CONMIN = data['cm_con_vals_CONMIN']
fc_cd_vals_CONMIN = data['fc_cd_vals_CONMIN']

# Now you can use these arrays for plotting or any other analysis

fig1 = plt.figure(figsize = (12,12))
real_fc_cd_vals_CONMIN = [np.real(fc_cd_val) for fc_cd_val in fc_cd_vals_CONMIN]
iterations_CONMIN = np.arange(len(real_fc_cd_vals_CONMIN))
plt.plot(iterations_CONMIN, real_fc_cd_vals_CONMIN, marker='.', lw=2, color='r')
plt.xlabel('iterations')
plt.ylabel('Cd value')
plt.show()
plt.pause(60)

fig2 = plt.figure(figsize = (12,12))
real_cl_con_vals_CONMIN = [np.real(cl_con_val) for cl_con_val in cl_con_vals_CONMIN]
iterations_CONMIN = np.arange(len(real_cl_con_vals_CONMIN))
plt.plot(iterations_CONMIN, real_cl_con_vals_CONMIN, marker='.', lw=2, color='r')
plt.xlabel('iterations')
plt.ylabel('CL constraint violation')
plt.show()
plt.pause(60)

fig3 = plt.figure(figsize = (12,12))
real_cm_con_vals_CONMIN = [np.real(cm_con_val) for cm_con_val in cm_con_vals_CONMIN]
iterations_CONMIN = np.arange(len(real_cm_con_vals_CONMIN))
plt.plot(iterations_CONMIN, real_cm_con_vals_CONMIN, marker='.', lw=2, color='r')
plt.xlabel('iterations')
plt.ylabel('CM constraint violation')
plt.show()
plt.pause(60)