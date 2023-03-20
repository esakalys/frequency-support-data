import functions as f
import matplotlib.pyplot as plt
import numpy as np

# Program used to carry out the inertial + droop study analysis

scenarios = ['20MW', '25MW']

limitedF = [f'frequency {scenario}.mat' for scenario in scenarios]
limitedR = [f'rocof {scenario}.mat' for scenario in scenarios]
limitedV = [f'power-vsc {scenario}.mat' for scenario in scenarios]

dsF = f.importData(limitedF, 'data/v2-data/9-limited-capacity-study')
dsR = f.importData(limitedR, 'data/v2-data/9-limited-capacity-study')
dsV = f.importData(limitedV, 'data/v2-data/9-limited-capacity-study')

i = 0
for key in dsF.keys():
    print(f'Case {scenarios[i]}:')
    t0_index = dsF[key]['Time'].index(0.0)
    index = range(t0_index)

    ds = np.delete(dsF[key]['Value'], index)

    f_min = round(min(ds), 4)
    f_delta = round(f_min - 50, 4)
    f_ss = round(ds[-1]-50, 4)
    print(f'Max delta frequency = {f_delta}')
    print(f'Steady state delta frequency = {f_ss}')
    i += 1
    print()

i = 0
for key in dsR.keys():
    print(f'Case {scenarios[i]}:')
    t0_index = dsR[key]['Time'].index(0.0)
    index = range(t0_index)

    ds = np.delete(dsR[key]['Value'], index)

    r_max = round(max(abs(ds)), 4)
    print(f'Maximum RoCoF = {r_max}')
    i += 1
    print()

i = 0
for key in dsV.keys():
    print(f'Case {scenarios[i]}:')
    t0_index = dsV[key]['Time'].index(0.0)
    index = range(t0_index)

    ds = np.delete(dsV[key]['Value'], index)

    cleanTime = map(lambda t: round(t, 7), dsV[key]['Time'])
    dsV[key]['Time'] = list(cleanTime)

    energy = round(f.integrate(dsV[key], 5.0, 10.0), 4)

    p_max = round(max(abs(ds)), 4)
    p_ss = round(ds[-1], 4)
    print(f'Maximum VSC Power Output = {p_max} MW')
    print(f'VSC Energy Used = {energy} MJ')
    print(f'Steady State VSC Power Output = {p_ss} MW')
    i += 1
    print()