import functions as f
import matplotlib.pyplot as plt

# Program used to plot the limited capacity study vsc power output data

colors = ['#0789FA', '#F10A0A']

f_limited = 'power-vsc.mat'
f_unlimited = 'power-vsc 15MW 2.5s.mat'

ds_limited = f.importData(f_limited, 'data/v2-data/10-limited-capacity-study', single=True)
ds_unlimited = f.importData(f_unlimited, 'data/v2-data/7-inertial-droop-study', single=True)

plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds_limited[f_limited]['Time'], ds_limited[f_limited]['Value'], color=colors[1], linewidth=1.4, label='Limited Capacity')
plt.plot(ds_unlimited[f_unlimited]['Time'], ds_unlimited[f_unlimited]['Value'], color=colors[0], linewidth=1.4, label='Unlimited Capacity')

plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
plt.title('VSC Power Output', pad=20)
plt.xlabel('Time, s')
plt.ylabel('Power, MW')
plt.xlim([0, 35])
plt.ylim([-2, 32])
plt.legend(loc='lower right')
plt.savefig(f'plots/v2-plots/10-limited-capacity-power-vsc.jpg', dpi=400, bbox_inches='tight')
