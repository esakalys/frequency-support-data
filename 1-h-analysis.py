import functions as f
import matplotlib.pyplot as plt

# Program used to carry out the analysis for the generator inertia study

scenarios = ['5s', '4s', '3s', '2s']

filesF = [f'frequency {scenario}.mat' for scenario in scenarios]
filesR = [f'rocof {scenario}.mat' for scenario in scenarios]

dsF = f.importData(filesF, 'data/v2-data/1-h-study')
dsR = f.importData(filesR, 'data/v2-data/1-h-study')

i = 0
for key in dsF.keys():
    f_min = round(min(dsF[key]['Value']), 4)
    f_delta = round(f_min - 50, 4)
    f_ss = round(dsF[key]['Value'][-1], 4)
    print(f'Case {scenarios[i]}: Minimum frequency = {f_min}, delta = {f_delta}')
    print(f'Case {scenarios[i]}: Steady-State frequency = {f_ss}')
    i += 1

i = 0
for key in dsR.keys():
    r_max = round(max(abs(dsR[key]['Value'])), 4)
    print(f'Case {scenarios[i]}: Maximum RoCoF = {r_max}')
    i += 1