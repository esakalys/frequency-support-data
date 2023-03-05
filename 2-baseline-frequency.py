import functions as f
import matplotlib.pyplot as plt

# Program used to plot the baseline frequency data

scenarios = ['5MW', '10MW', '15MW']
inertia = ['5s', '2.5s']
colors = ['#0789FA', '#7C4A82', '#F10A0A']

for h in inertia:
    files = [f'frequency {scenario} {h}.mat' for scenario in scenarios]

    ds = f.importData(files, 'data/v2-data/2-baseline-study')

    plt.figure(figsize=(6, 4), dpi=400)

    i = 0
    for key in ds.keys():
        plt.plot(ds[key]['Time'], ds[key]['Value'], color=colors[i], linewidth=1.4, label=f'\u0394P = +{scenarios[i]}')
        i += 1

    plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
    plt.title(f'Grid Frequency  |  H = {h}', pad=20)
    plt.xlabel('Time, s')
    plt.ylabel('Frequency, Hz')
    plt.xlim([0, 35])
    plt.ylim([48.8, 50.4])
    plt.legend(loc='lower right')
    plt.savefig(f'plots/v2-plots/2-baseline-frequency-{h}.jpg', dpi=400, bbox_inches='tight')
