import functions as f
import matplotlib.pyplot as plt

# Program used to plot the inertial study rocof data

scenarios = ['5MW', '10MW', '15MW']
inertia = ['5s', '2.5s']
colors = ['#0789FA', '#F10A0A']

for h in inertia:
    for scenario in scenarios:
        file = f'rocof {scenario} {h}.mat'

        dsInt = f.importData(file, 'data/v2-data/5-inertial-study', single=True)
        dsBase = f.importData(file, 'data/v2-data/2-baseline-study', single=True)

        plt.figure(figsize=(6, 4), dpi=400)

        plt.plot(dsInt[file]['Time'], dsInt[file]['Value'], color=colors[0], linewidth=1.4, label=f'With VSC')
        plt.plot(dsBase[file]['Time'], dsBase[file]['Value'], color=colors[1], linewidth=1.4, label=f'Without VSC')

        plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
        plt.title(f'Grid RoCoF  |  H(Gen) = {h}  |  \u0394P = +{scenario}', pad=20)
        plt.xlabel('Time, s')
        plt.ylabel('RoCoF, Hz/s')
        plt.xlim([0, 25])
        plt.ylim([-0.55, 0.55])
        plt.legend(loc='upper right')
        plt.savefig(f'plots/v2-plots/5-inertial-rocof-{h}-{scenario}.jpg', dpi=400, bbox_inches='tight')
