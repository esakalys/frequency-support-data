import functions as f
import matplotlib.pyplot as plt

# Program used to plot the overfrequency study VSC power output data

inertia = ['2.5s']
colors = ['#0789FA', '#F10A0A']

files = [f'power-vsc {h}.mat' for h in inertia]

ds = f.importData(files, 'data/v2-data/8-overfrequency-study')

plt.figure(figsize=(6, 4), dpi=400)

i = 0
z = 10
for key in ds.keys():
    plt.plot(ds[key]['Time'], ds[key]['Value'], color=colors[i], linewidth=1.2, label=f'H(Gen) = {inertia[i]}', zorder=z)
    i += 1
    z -= 1

plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
plt.title(f'VSC Power Output', pad=20)
plt.xlabel('Time, s')
plt.ylabel('Power, MW')
plt.xlim([0, 35])
plt.ylim([-10, 2])
plt.legend(loc='upper right')
plt.savefig(f'plots/v2-plots/8-report-overfrequency-power-vsc.jpg', dpi=400, bbox_inches='tight')
