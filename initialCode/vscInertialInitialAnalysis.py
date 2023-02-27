
import matplotlib.pyplot as plt
import functions as f

# Program used perform initial analysis of the frequency response of the grid with the VSC contributing while under inertial control

scenarios = ['+10', '+20', '+30', '+40', '+50']
colors = ["#409823","#E47928"]

for scenario in scenarios:
    files = [f'Frequency {scenario}.mat', f'Frequency {scenario} 5s.mat']

    ds = f.importData(files, 'data/matFiles')

    for file in files:
        file.replace('.mat', '')

    plt.figure(figsize=(6, 4), dpi=400)

    plt.plot(ds[files[0]]['Time'], ds[files[0]]['Value'], color=colors[0], linewidth=1, label='With VSC')
    plt.plot(ds[files[1]]['Time'], ds[files[1]]['Value'], color=colors[1], linewidth=2, label='Without VSC')

    plt.grid()
    plt.title(f'VSC Intervention - Inertial - {scenario}MW')
    plt.xlabel('Time, s')
    plt.ylabel('Frequency, Hz')
    plt.legend(loc='upper right')
    plt.savefig(f'initialPlots/VSCinertial{scenario}.jpg', dpi=400)
