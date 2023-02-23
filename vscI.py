import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import mat73

scenarios = ['+10', '+20', '+30', '+40', '+50']
dir = os.getcwd()

for scenario in scenarios:
    files = [f'Frequency {scenario}', f'Frequency {scenario} 5s']

    colors = ["#409823","#E47928"]

    ds = {}

    for file in files:
        mat = mat73.loadmat(f'{dir}/matFiles/{file}.mat')
        x = mat['x'][1]
        t = mat['x'][0]

        data = {'Time': t, 'Value': x}
        ds[file] = data

    plt.figure(figsize=(6, 4), dpi=400)

    plt.plot(ds[files[0]]['Time'], ds[files[0]]['Value'], color=colors[0], linewidth=1, label='With VSC')
    plt.plot(ds[files[1]]['Time'], ds[files[1]]['Value'], color=colors[1], linewidth=2, label='Without VSC')

    plt.grid()
    plt.title(f'VSC Intervention - Inertial - {scenario}MW')
    plt.xlabel('Time, s')
    plt.ylabel('Frequency, Hz')
    plt.legend(loc='upper right')
    plt.savefig(f'plots/VSCinertial{scenario}.jpg', dpi=400)
