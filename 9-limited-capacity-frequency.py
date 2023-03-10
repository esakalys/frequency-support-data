import functions as f
import matplotlib.pyplot as plt

# Program used to plot the limited capacity study frequency data

colors = ['#0789FA', '#555FAA', '#A3345A', '#F10A0A']

# Select if baseline data should be included
baseline = False

if not baseline:
  colors = ['#0789FA', '#7C4A82', '#F10A0A']

f_baseline = 'frequency 15MW 2.5s.mat'
f_limited5 = 'frequency 25MW.mat'
f_limited10 = 'frequency 20MW.mat'
f_unlimited = 'frequency 15MW 2.5s.mat'

ds_baseline = f.importData(f_baseline, 'data/v2-data/2-baseline-study', single=True)
ds_limited5 = f.importData(f_limited5, 'data/v2-data/9-limited-capacity-study', single=True)
ds_limited10 = f.importData(f_limited10, 'data/v2-data/9-limited-capacity-study', single=True)
ds_unlimited = f.importData(f_unlimited, 'data/v2-data/7-inertial-droop-study', single=True)

plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds_unlimited[f_unlimited]['Time'], ds_unlimited[f_unlimited]['Value'], color=colors[0], linewidth=1.2, label='Capacity = 30MW')
plt.plot(ds_limited10[f_limited10]['Time'], ds_limited10[f_limited10]['Value'], color=colors[1], linewidth=1.2, label='Capacity = 10MW')
plt.plot(ds_limited5[f_limited5]['Time'], ds_limited5[f_limited5]['Value'], color=colors[2], linewidth=1.2, label='Capacity = 5MW')
if baseline:
  plt.plot(ds_baseline[f_baseline]['Time'], ds_baseline[f_baseline]['Value'], color=colors[3], linewidth=1.2, label='Baseline')

plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
plt.title('Grid Frequency', pad=20)
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.xlim([0, 35])
plt.legend(loc='upper right')

if baseline:
  plt.ylim([48.8, 50.4])
  plt.savefig(f'plots/v2-plots/9-limited-capacity-frequency-with-baseline.jpg', dpi=400, bbox_inches='tight')
else:
  plt.ylim([49.5, 50.1])
  plt.savefig(f'plots/v2-plots/9-limited-capacity-frequency-no-baseline.jpg', dpi=400, bbox_inches='tight')
