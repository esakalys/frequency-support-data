import functions as f
import matplotlib.pyplot as plt

# Program used to plot the inertial + droop study VSC power output data

scenarios = ['10MW']
inertia = ['2.5s']
colors = ['#0789FA', '#7C4A82', '#F10A0A']

for h in inertia:
    files = [f'power-vsc {scenario} {h}.mat' for scenario in scenarios]

    ds = f.importData(files, 'data/v2-data/7-inertial-droop-study')

    plt.figure(figsize=(6, 4), dpi=400)

    i = 0
    for key in ds.keys():
        plt.plot(ds[key]['Time'], ds[key]['Value'], color=colors[i], linewidth=1.4, label=f'\u0394P = +{scenarios[i]}')
        i += 1

    plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
    plt.title(f'VSC Power Output  |  H(Gen) = {h}  |  \u0394P = +10MW', pad=20)
    plt.xlabel('Time, s')
    plt.ylabel('Power, MW')
    plt.xlim([0, 35])
    plt.ylim([-2, 10])
    plt.savefig(f'plots/v2-plots/7-report-inertial-droop-power-vsc-{h}.jpg', dpi=400, bbox_inches='tight')
