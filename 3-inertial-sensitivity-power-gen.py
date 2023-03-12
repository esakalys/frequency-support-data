import functions as f
import matplotlib.pyplot as plt

# Program used to plot the inertial sensitivity study generator power data

scenarios = ['1s', '2s', '3s', '4s', '5s']
inertia = ['5s', '2.5s']
colors = ['#0789FA', '#4269BE', '#7C4A82', '#B72A46', '#F10A0A']

for h in inertia:
    files = [f'power-gen {scenario} {h}.mat' for scenario in scenarios]

    ds = f.importData(files, 'data/v2-data/3-inertial-sensitivity-study')

    plt.figure(figsize=(6, 4), dpi=400)

    i = 0
    z = 10
    for key in ds.keys():
        plt.plot(ds[key]['Time'], ds[key]['Value'], color=colors[i], linewidth=1.2, label=f'H(VSC) = {scenarios[i]}', zorder=z)
        i += 1
        z -= 1

    plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
    plt.title(f'Generator Power Ouput  |  H(Gen) = {h}', pad=20)
    plt.xlabel('Time, s')
    plt.ylabel('Power, MW')
    plt.xlim([0, 35])
    plt.ylim([48, 62])
    plt.legend(loc='lower right')
    plt.savefig(f'plots/v2-plots/3-inertial-sensitivity-power-gen-{h}.jpg', dpi=400, bbox_inches='tight')
