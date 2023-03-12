import functions as f
import matplotlib.pyplot as plt

# Program used to plot the droop sensitivity study rocof data

scenarios = ['1', '2', '3', '4', '5']
inertia = ['5s', '2.5s']
colors = ['#0789FA', '#4269BE', '#7C4A82', '#B72A46', '#F10A0A']

for h in inertia:
    files = [f'rocof {scenario} {h}.mat' for scenario in scenarios]

    ds = f.importData(files, 'data/v2-data/4-droop-sensitivity-study')

    plt.figure(figsize=(6, 4), dpi=400)

    i = 0
    for key in ds.keys():
        plt.plot(ds[key]['Time'], ds[key]['Value'], color=colors[i], linewidth=1.2, label=f'Droop = {scenarios[i]}')
        i += 1

    plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
    plt.title(f'Grid RoCoF  |  H(Gen) = {h}', pad=20)
    plt.xlabel('Time, s')
    plt.ylabel('RoCoF, Hz/s')
    plt.xlim([0, 35])
    plt.ylim([-0.15, 0.05])
    plt.legend(loc='lower right')
    plt.savefig(f'plots/v2-plots/4-droop-sensitivity-rocof-{h}.jpg', dpi=400, bbox_inches='tight')
