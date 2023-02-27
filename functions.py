import os
import mat73

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
        if 'Power' in files:
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
            if 'Power' in file:
                x = [(-1/1000000)*value for value in x]

            data = {'Time': t, 'Value': x}
            ds[file] = data

    return ds

