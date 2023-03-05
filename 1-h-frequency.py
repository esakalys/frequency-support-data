import functions as f
import matplotlib.pyplot as plt

# Program used to plot the effect of generator inertia (H) on frequency

scenarios = ['5s', '4s', '3s', '2s']
colors = ['#0789FA', '#555FAA', '#A3345A', '#F10A0A']

files = [f'frequency {scenario}.mat' for scenario in scenarios]

ds = f.importData(files, 'data/v2-data/1-h-study')

plt.figure(figsize=(6, 4), dpi=400)

i = 0
for key in ds.keys():
    plt.plot(ds[key]['Time'], ds[key]['Value'], color=colors[i], linewidth=1.4, label=f'H = {scenarios[i]}')
    i += 1

plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
plt.title('Grid Frequency  |  \u0394P = +10 MW', pad=20)
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.xlim([4, 14])
plt.ylim([49.4, 50.2])
plt.legend(loc='lower right')
plt.savefig('plots/v2-plots/1-h-frequency.jpg', dpi=400, bbox_inches='tight')
