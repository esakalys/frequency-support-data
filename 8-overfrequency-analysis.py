import functions as f
import matplotlib.pyplot as plt
import numpy as np

# Program used to carry out the inertial + droop study analysis

inertia = ['5s', '2.5s']

for h in inertia:
    
    filesF = [f'frequency {h}.mat', f'frequency base {h}.mat']
    filesR = [f'rocof {h}.mat', f'rocof base {h}.mat']
    fileV = f'power-vsc {h}.mat'

    dsF = f.importData(filesF, 'data/v2-data/8-overfrequency-study')
    dsR = f.importData(filesR, 'data/v2-data/8-overfrequency-study')
    dsV = f.importData(fileV, 'data/v2-data/8-overfrequency-study', single=True)

    print(f'Generator Inertia = {h}')
    print()

    i = 0
    t0_index = dsF[filesF[0]]['Time'].index(0.0)
    index = range(t0_index)

    ds = np.delete(dsF[filesF[0]]['Value'], index)
    ds_base = np.delete(dsF[filesF[1]]['Value'], index)

    f_max = round(max(ds), 4)
    f_delta = round(f_max - 50, 4)
    f_max_base = round(max(ds_base), 4)
    f_delta_base = round(f_max_base - 50, 4)
    f_ss = round(ds[-1]-50, 4)
    f_ss_base = round(ds_base[-1]-50, 4)
    print(f'Max delta frequency = {f_delta}')
    print(f'Baseline Max delta frequency = {f_delta_base}')
    print(f'Steady state delta frequency = {f_ss}')
    print(f'Baseline Steady state delta frequency = {f_ss_base}')
    i += 1
    print()

    i = 0
    t0_index = dsR[filesR[0]]['Time'].index(0.0)
    index = range(t0_index)

    ds = np.delete(dsR[filesR[0]]['Value'], index)
    ds_base = np.delete(dsR[filesR[1]]['Value'], index)

    r_max = round(max(abs(ds)), 4)
    r_max_base = round(max(abs(ds_base)), 4)
    print(f'Maximum RoCoF = {r_max}')
    print(f'Baseline Max RoCoF = {r_max_base}')
    i += 1
    print()

    i = 0
    t0_index = dsV[fileV]['Time'].index(0.0)
    index = range(t0_index)

    ds = np.delete(dsV[fileV]['Value'], index)

    cleanTime = map(lambda t: round(t, 7), dsV[fileV]['Time'])
    dsV[fileV]['Time'] = list(cleanTime)

    energy = round(f.integrate(dsV[fileV], 5.0, 10.0), 4)

    p_min = round(min(ds), 4)
    p_ss = round(ds[-1], 4)
    print(f'Maximum VSC Power Output = {p_min} MW')
    print(f'VSC Energy Used = {energy} MJ')
    print(f'Steady State VSC Power Output = {p_ss} MW')
    i += 1
    print()