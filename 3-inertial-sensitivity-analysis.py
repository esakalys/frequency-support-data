import functions as f
import matplotlib.pyplot as plt
import numpy as np

# Program used to carry out the baseline study analysis

scenarios = ['1s', '2s', '3s', '4s', '5s']
inertia = ['5s', '2.5s']

for h in inertia:
    
    filesF = [f'frequency {scenario} {h}.mat' for scenario in scenarios]
    filesR = [f'rocof {scenario} {h}.mat' for scenario in scenarios]
    filesV = [f'power-vsc {scenario} {h}.mat' for scenario in scenarios]

    dsF = f.importData(filesF, 'data/v2-data/3-inertial-sensitivity-study')
    dsR = f.importData(filesR, 'data/v2-data/3-inertial-sensitivity-study')
    dsV = f.importData(filesV, 'data/v2-data/3-inertial-sensitivity-study')

    print(f'Generator Inertia = {h}')

    i = 0
    for key in dsF.keys():

        t0_index = dsF[key]['Time'].index(0.0)
        index = range(t0_index)

        ds = np.delete(dsF[key]['Value'], index)

        f_min = round(min(ds), 4)
        f_delta = round(f_min - 50, 4)
        f_ss = round(ds[-1], 4)
        print(f'Case {scenarios[i]}: Minimum frequency = {f_min}, delta = {f_delta}')
        print(f'Case {scenarios[i]}: Steady-State frequency = {f_ss}')
        i += 1

    i = 0
    for key in dsR.keys():

        t0_index = dsR[key]['Time'].index(0.0)
        index = range(t0_index)

        ds = np.delete(dsR[key]['Value'], index)

        r_max = round(max(abs(ds)), 4)
        print(f'Case {scenarios[i]}: Maximum RoCoF = {r_max}')
        i += 1

    i = 0
    for key in dsV.keys():

        t0_index = dsV[key]['Time'].index(0.0)
        index = range(t0_index)

        ds = np.delete(dsV[key]['Value'], index)

        p_max = round(max(abs(ds)), 4)
        print(f'Case {scenarios[i]}: Maximum VSC Power Output = {p_max}')
        i += 1