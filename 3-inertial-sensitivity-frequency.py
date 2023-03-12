import functions as f
import matplotlib.pyplot as plt

# Program used to plot the inertial sensitivity study frequency data

scenarios = ['1s', '2s', '3s', '4s', '5s']
inertia = ['5s', '2.5s']
colors = ['#0789FA', '#4269BE', '#7C4A82', '#B72A46', '#F10A0A']

for h in inertia:
    files = [f'frequency {scenario} {h}.mat' for scenario in scenarios]

    ds = f.importData(files, 'data/v2-data/3-inertial-sensitivity-study')

    plt.figure(figsize=(6, 4), dpi=400)

    i = 0
    for key in ds.keys():
        plt.plot(ds[key]['Time'], ds[key]['Value'], color=colors[i], linewidth=1.4, label=f'H(VSC) = {scenarios[i]}')
        i += 1

    plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
    plt.title(f'Grid Frequency  |  H(Gen) = {h}', pad=20)
    plt.xlabel('Time, s')
    plt.ylabel('Frequency, Hz')
    plt.xlim([0, 35])
    plt.ylim([49.7, 50.1])
    plt.legend(loc='upper right')
    plt.savefig(f'plots/v2-plots/3-inertial-sensitivity-frequency-{h}.jpg', dpi=400, bbox_inches='tight')
