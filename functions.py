import os
import mat73
import numpy as np

# Function used to import the simulation data stored in .mat files
def importData(files, location, trimTime=True, single=False):

    dir = os.getcwd()
    ds = {}

    if single:
        mat = mat73.loadmat(f'{dir}/{location}/{files}')
        x = mat['x'][1]
        if trimTime:
            t = [value-10 for value in mat['x'][0]]
        else:
            t = mat['x'][0]

        # Define positive power as power from generator / vsc to grid in MW
        if 'power' in files:
            x = [(-1/1000000)*value for value in x]

        data = {'Time': t, 'Value': x}
        ds[files] = data
    else:
        for file in files:
            mat = mat73.loadmat(f'{dir}/{location}/{file}')
            x = mat['x'][1]
            if trimTime:
                t = [value-10 for value in mat['x'][0]]
            else:
                t = mat['x'][0]

            # Define positive power as power from generator / vsc to grid in MW
            if 'power' in file:
                x = [(-1/1000000)*value for value in x]

            data = {'Time': t, 'Value': x}
            ds[file] = data

    return ds

# Function used to import 3 phase simulation data stored in .mat files
def import3phData(files, location, trimTime=True):

    dir = os.getcwd()
    ds = {}

    for file in files:
        mat = mat73.loadmat(f'{dir}/{location}/{file}')
        a = mat['x'][1]
        b = mat['x'][2]
        c = mat['x'][3]
        if trimTime:
            t = [value-10 for value in mat['x'][0]]
        else:
            t = mat['x'][0]

        data = {'Time': t, 'a': a, 'b': b, 'c': c}
        ds[file] = data

    return ds

# Function for integrating the VSC power output
def integrate(data, t1, t2, tStep=5e-6):
    sum = 0.0

    t1_index = data['Time'].index(t1)
    t2_index = data['Time'].index(t2)

    ds = np.array(data['Value'][t1_index:t2_index])

    for value in ds:
        sum += value*tStep
    return sum
