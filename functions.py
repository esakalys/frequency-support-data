import os
import mat73

def importData(files, location):

    dir = os.getcwd()
    ds = {}
    for file in files:
        mat = mat73.loadmat(f'{dir}/{location}/{file}')
        x = mat['x'][1]
        t = [value-10 for value in mat['x'][0]]

        # Define positive power as power from generator / vsc to grid
        if 'Power' in file:
            x = [(-1/1000000)*value for value in x]

        data = {'Time': t, 'Value': x}
        file = file.replace('.mat', '')
        ds[file] = data

    return ds

