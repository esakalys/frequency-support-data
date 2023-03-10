import functions as f
import matplotlib.pyplot as plt

# Program used to plot the limited capacity study vsc power output data data

colors = ['#0789FA', '#7C4A82', '#F10A0A']

f_limited5 = 'power-vsc 25MW.mat'
f_limited10 = 'power-vsc 20MW.mat'
f_unlimited = 'power-vsc 15MW 2.5s.mat'

ds_limited5 = f.importData(f_limited5, 'data/v2-data/9-limited-capacity-study', single=True)
ds_limited10 = f.importData(f_limited10, 'data/v2-data/9-limited-capacity-study', single=True)
ds_unlimited = f.importData(f_unlimited, 'data/v2-data/7-inertial-droop-study', single=True)

plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds_unlimited[f_unlimited]['Time'], ds_unlimited[f_unlimited]['Value'], color=colors[0], linewidth=1.2, label='Capacity = 30MW')
plt.plot(ds_limited10[f_limited10]['Time'], ds_limited10[f_limited10]['Value'], color=colors[1], linewidth=1.2, label='Capacity = 10MW')
plt.plot(ds_limited5[f_limited5]['Time'], ds_limited5[f_limited5]['Value'], color=colors[2], linewidth=1.2, label='Capacity = 5MW')

plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
plt.title('VSC Power Output', pad=20)
plt.xlabel('Time, s')
plt.ylabel('Power, MW')
plt.xlim([0, 35])
plt.legend(loc='lower right')

plt.ylim([-2, 32])
plt.savefig(f'plots/v2-plots/9-limited-capacity-power-vsc.jpg', dpi=400, bbox_inches='tight')
