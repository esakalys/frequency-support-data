import functions as f
import matplotlib.pyplot as plt
import numpy as np

# Program used to carry out the droop study analysis

scenarios = ['5MW', '10MW', '15MW']
inertia = ['5s', '2.5s']

for h in inertia:
    
    filesF = [f'frequency {scenario} {h}.mat' for scenario in scenarios]
    filesR = [f'rocof {scenario} {h}.mat' for scenario in scenarios]
    filesV = [f'power-vsc {scenario} {h}.mat' for scenario in scenarios]

    dsF = f.importData(filesF, 'data/v2-data/6-droop-study')
    dsF_base = f.importData(filesF, 'data/v2-data/2-baseline-study')
    dsR = f.importData(filesR, 'data/v2-data/6-droop-study')
    dsR_base = f.importData(filesR, 'data/v2-data/2-baseline-study')
    dsV = f.importData(filesV, 'data/v2-data/6-droop-study')

    print(f'Generator Inertia = {h}')

    i = 0
    for key in dsF.keys():

        t0_index = dsF[key]['Time'].index(0.0)
        index = range(t0_index)

        ds = np.delete(dsF[key]['Value'], index)
        ds_base = np.delete(dsF_base[key]['Value'], index)

        f_min = round(min(ds), 4)
        f_delta = round(f_min - 50, 4)
        f_min_base = round(min(ds_base), 4)
        f_delta_base = round(f_min_base - 50, 4)
        f_ss = round(ds[-1], 4)
        f_ss_base = round(ds_base[-1], 4)
        print(f'Case {scenarios[i]}: Max delta frequency = {f_delta}')
        print(f'Case {scenarios[i]}: Baseline Max delta frequency = {f_delta_base}')
        print(f'Case {scenarios[i]}: Steady state frequency = {f_ss}')
        print(f'Case {scenarios[i]}: Baseline Steady state frequency = {f_ss_base}')
        i += 1

    i = 0
    for key in dsR.keys():

        t0_index = dsR[key]['Time'].index(0.0)
        index = range(t0_index)

        ds = np.delete(dsR[key]['Value'], index)
        ds_base = np.delete(dsR_base[key]['Value'], index)

        r_max = round(max(abs(ds)), 4)
        r_max_base = round(max(abs(ds_base)), 4)
        print(f'Case {scenarios[i]}: Maximum RoCoF = {r_max}')
        print(f'Case {scenarios[i]}: Baseline Max RoCoF = {r_max_base}')
        i += 1

    i = 0
    for key in dsV.keys():

        t0_index = dsV[key]['Time'].index(0.0)
        index = range(t0_index)

        ds = np.delete(dsV[key]['Value'], index)

        p_max = round(max(abs(ds)), 4)
        p_ss = round(ds[-1], 4)
        print(f'Case {scenarios[i]}: Maximum VSC Power Output = {p_max}')
        print(f'Case {scenarios[i]}: Steady State VSC Power Output = {p_ss}')
        i += 1