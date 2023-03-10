import functions as f
import matplotlib.pyplot as plt

# Program used to plot the baseline frequency data
scenarios = ['+5MW', '+10MW', '+20MW']

colors = ['#6386F1', '#3B53A8', '#13205F']

files = [f'Frequency {scenario} 5s.mat' for scenario in scenarios]

ds = f.importData(files, 'data/baselineMat')

plt.figure(figsize=(6, 4), dpi=400)

i = 0
for key in ds.keys():
    plt.plot(ds[key]['Time'], ds[key]['Value'], color=colors[i], linewidth=2, label=scenarios[i])
    i += 1

plt.grid()
plt.title('Baseline Frequency')
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.xlim([0, 35])
plt.legend(loc='lower right')
plt.savefig(f'reportPlots/baselineFrequency.jpg', dpi=400)
