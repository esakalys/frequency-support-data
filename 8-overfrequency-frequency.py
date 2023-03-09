import functions as f
import matplotlib.pyplot as plt

# Program used to plot the overfrequency study frequency data

inertia = ['5s', '2.5s']
colors = ['#0789FA', '#F10A0A']

for h in inertia:
    fileInt = f'frequency {h}.mat'
    fileBase = f'frequency base {h}.mat'

    dsInt = f.importData(fileInt, 'data/v2-data/8-overfrequency-study', single=True)
    dsBase = f.importData(fileBase, 'data/v2-data/8-overfrequency-study', single=True)

    plt.figure(figsize=(6, 4), dpi=400)

    plt.plot(dsInt[fileInt]['Time'], dsInt[fileInt]['Value'], color=colors[0], linewidth=1.4, label=f'With VSC')
    plt.plot(dsBase[fileBase]['Time'], dsBase[fileBase]['Value'], color=colors[1], linewidth=1.4, label=f'Without VSC')

    plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
    plt.title(f'Grid Frequency  |  H(Gen) = {h}', pad=20)
    plt.xlabel('Time, s')
    plt.ylabel('Frequency, Hz')
    plt.xlim([0, 35])
    plt.ylim([49.8, 50.6])
    plt.legend(loc='upper right')
    plt.savefig(f'plots/v2-plots/8-overfrequency-frequency-{h}.jpg', dpi=400, bbox_inches='tight')
