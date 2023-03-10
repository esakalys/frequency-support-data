import functions as f
import matplotlib.pyplot as plt

# Program used to plot the effect of generator inertia (H) on frequency

scenarios = ['5s', '4s', '3s', '2s', '1s']
colors = ['#3B53A8', '#5C3E7E', '#7C2A54', '#9D152A', '#BD0000']

files = [f'Frequency +10MW {scenario}.mat' for scenario in scenarios]

ds = f.importData(files, 'data/hMat')

plt.figure(figsize=(6, 4), dpi=400)

i = 0
for key in ds.keys():
    plt.plot(ds[key]['Time'], ds[key]['Value'], color=colors[i], linewidth=2, label=scenarios[i])
    i += 1

plt.grid()
plt.title('Effect of Varying H on Grid Frequency')
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.xlim([4, 15])
plt.ylim([49.2, 50.3])
plt.legend(loc='lower right')
plt.savefig(f'reportPlots/hFrequency.jpg', dpi=400)
