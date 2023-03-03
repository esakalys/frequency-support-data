import functions as f
import matplotlib.pyplot as plt

# Program used to plot the effect of generator inertia (H) on rocof

scenarios = ['5s', '4s', '3s', '2s', '1s']
colors = ['#3B53A8', '#5C3E7E', '#7C2A54', '#9D152A', '#BD0000']

files = [f'rocof +10MW {scenario}.mat' for scenario in scenarios]

ds = f.importData(files, 'data/hMat')

plt.figure(figsize=(6, 4), dpi=400)

i = 0
for key in ds.keys():
    plt.plot(ds[key]['Time'], ds[key]['Value'], color=colors[i], linewidth=2, label=scenarios[i])
    i += 1

plt.grid()
plt.title('Effect of Varying H on Grid RoCoF')
plt.xlabel('Time, s')
plt.ylabel('RoCoF, Hz/s')
plt.xlim([4, 15])
plt.ylim([-0.055, 0.055])
plt.legend(loc='lower right')
plt.savefig(f'reportPlots/hRocof.jpg', dpi=400)