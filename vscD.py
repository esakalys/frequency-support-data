import matplotlib.pyplot as plt
import functions as f

scenarios = ['+10', '+20', '+30', '+40', '+50']
colors = ["#409823", "#E47928"]

for scenario in scenarios:
    files = [f'Frequency Droop {scenario}', f'Frequency {scenario} 5s']

    ds = f.importData(files, 'matFiles')

    plt.figure(figsize=(6, 4), dpi=400)

    plt.plot(ds[files[0]]['Time'], ds[files[0]]['Value'], color=colors[0], linewidth=1, label='With VSC')
    plt.plot(ds[files[1]]['Time'], ds[files[1]]['Value'], color=colors[1], linewidth=2, label='Without VSC')

    plt.grid()
    plt.title(f'VSC Intervention - Droop - {scenario}MW')
    plt.xlabel('Time, s')
    plt.ylabel('Frequency, Hz')
    plt.legend(loc='upper right')
    plt.savefig(f'plots/VSCdroop{scenario}.jpg', dpi=400)
