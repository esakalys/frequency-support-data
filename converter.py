import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import mat73

# Program to convert the .mat files to .csv files

dir = os.getcwd()
files = os.listdir(f'{dir}/matFiles')

colorsBlue = ["#0A2136","#133557","#1C4977","#265E98","#2F72B9","#3886D9","#419AFA"]
colorsRed = ["#751414","#8B1D1D","#A12626","#B83030","#CE3939","#E44242","#FA4B4B"]
colorsComp = ["#409823","#E47928"]

ds = {}

for file in files:
    if '.mat' in file:
        mat = mat73.loadmat(f'{dir}/matFiles/{file}')
        x = mat['x'][1]
        t = mat['x'][0]

        # Define positive power as power from generator to grid
        if 'Power' in file:
            x = [(-1/1000000)*value for value in x]

        data = {'Time': t, 'Value': x}
        file = file.replace('.mat', '')
        ds[file] = data

keys = ds.keys()

ufF5 = []
ufP5 = []
ofF5 = []
ofP5 = []

ufF10 = []
ufP10 = []
ofF10 = []
ofP10 = []

for key in keys:
    # Underfrequency events - 5s
    if ('Frequency' in key) and ('5s' in key and '+' in key or 'Base' in key):
        ufF5.append(key)
    elif ('Power' in key) and ('5s' in key and '+' in key or 'Base' in key):
        ufP5.append(key)
    # Overfrequency events - 5s
    if ('Frequency' in key) and ('5s' in key and '-' in key or 'Base' in key):
        ofF5.append(key)
    elif ('Power' in key) and ('5s' in key and '-' in key or 'Base' in key):
        ofP5.append(key)
    # Underfrequency events - 10s
    if ('Frequency' in key) and ('10s' in key and '+' in key or 'Base' in key):
        ufF10.append(key)
    elif ('Power' in key) and ('10s' in key and '+' in key or 'Base' in key):
        ufP10.append(key)
    # Overfrequency events - 10s
    if ('Frequency' in key) and ('10s' in key and '-' in key or 'Base' in key):
        ofF10.append(key)
    elif ('Power' in key) and ('10s' in key and '-' in key or 'Base' in key):
        ofP10.append(key)
    # Inertia comparison

ufF5.sort()
ufF5.insert(0, ufF5.pop())
ufP5.sort()
ufP5.insert(0, ufP5.pop())
ofF5.sort()
ofF5.insert(0, ofF5.pop())
ofP5.sort()
ofP5.insert(0, ofP5.pop())

ufF10.sort()
ufF10.insert(0, ufF10.pop())
ufP10.sort()
ufP10.insert(0, ufP10.pop())
ofF10.sort()
ofF10.insert(0, ofF10.pop())
ofP10.sort()
ofP10.insert(0, ofP10.pop())

plt.figure(figsize=(6, 4), dpi=400)
i = 0
for case in ufF5:
    plt.plot(ds[case]['Time'], ds[case]['Value'], color=colorsBlue[i], linewidth=1)
    i += 1
plt.grid()
plt.title('Underfrequency Events - Frequency - 5s')
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.legend(ufF5, loc='upper right')
plt.savefig('plots/UnderfrequencyEventsF5s.jpg', dpi=400)

plt.figure(figsize=(6, 4), dpi=400)
i = 0
for case in ufP5:
    plt.plot(ds[case]['Time'], ds[case]['Value'], color=colorsBlue[i], linewidth=1)
    i += 1
plt.grid()
plt.title('Underfrequency Events - Power - 5s')
plt.xlabel('Time, s')
plt.ylabel('Power, MW')
plt.legend(ufP5, loc='upper right')
plt.savefig('plots/UnderfrequencyEventsP5s.jpg', dpi=400)

plt.figure(figsize=(6, 4), dpi=400)
i = 0
for case in ofF5:
    plt.plot(ds[case]['Time'], ds[case]['Value'], color=colorsRed[i], linewidth=1)
    i += 1
plt.grid()
plt.title('Overfrequency Events - Frequency - 5s')
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.legend(ofF5, loc='upper right')
plt.savefig('plots/OverfrequencyEventsF5s.jpg', dpi=400)

plt.figure(figsize=(6, 4), dpi=400)
i = 0
for case in ofP5:
    plt.plot(ds[case]['Time'], ds[case]['Value'], color=colorsRed[i], linewidth=1)
    i += 1
plt.grid()
plt.title('Overfrequency Events - Power - 5s')
plt.xlabel('Time, s')
plt.ylabel('Power, MW')
plt.legend(ofP5, loc='upper right')
plt.savefig('plots/OverfrequencyEventsP5s.jpg', dpi=400)

plt.figure(figsize=(6, 4), dpi=400)
i = 0
for case in ufF10:
    plt.plot(ds[case]['Time'], ds[case]['Value'], color=colorsBlue[i], linewidth=1)
    i += 1
plt.grid()
plt.title('Underfrequency Events - Frequency - 10s')
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.legend(ufF10, loc='upper right')
plt.savefig('plots/UnderfrequencyEventsF10s.jpg', dpi=400)

plt.figure(figsize=(6, 4), dpi=400)
i = 0
for case in ufP10:
    plt.plot(ds[case]['Time'], ds[case]['Value'], color=colorsBlue[i], linewidth=1)
    i += 1
plt.grid()
plt.title('Underfrequency Events - Power - 10s')
plt.xlabel('Time, s')
plt.ylabel('Power, MW')
plt.legend(ufP10, loc='upper right')
plt.savefig('plots/UnderfrequencyEventsP10s.jpg', dpi=400)

plt.figure(figsize=(6, 4), dpi=400)
i = 0
for case in ofF10:
    plt.plot(ds[case]['Time'], ds[case]['Value'], color=colorsRed[i], linewidth=1)
    i += 1
plt.grid()
plt.title('Overfrequency Events - Frequency - 10s')
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.legend(ofF10, loc='upper right')
plt.savefig('plots/OverfrequencyEventsF10s.jpg', dpi=400)

plt.figure(figsize=(6, 4), dpi=400)
i = 0
for case in ofP10:
    plt.plot(ds[case]['Time'], ds[case]['Value'], color=colorsRed[i], linewidth=1)
    i += 1
plt.grid()
plt.title('Overfrequency Events - Power - 10s')
plt.xlabel('Time, s')
plt.ylabel('Power, MW')
plt.legend(ofP10, loc='upper right')
plt.savefig('plots/OverfrequencyEventsP10s.jpg', dpi=400)

# Comparisons between 5s and 10s

plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds['Frequency -10 5s']['Time'], ds['Frequency -10 5s']['Value'], color=colorsComp[0], linewidth=1)
plt.plot(ds['Frequency -10 10s']['Time'], ds['Frequency -10 10s']['Value'], color=colorsComp[1], linewidth=1)

plt.grid()
plt.title('Overfrequency Event -10MW')
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.legend(['H = 5s', 'H = 10s'], loc='upper right')
plt.savefig('plots/OverfrequencyComparison.jpg', dpi=400)

plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds['Frequency +10 5s']['Time'], ds['Frequency +10 5s']['Value'], color=colorsComp[0], linewidth=1)
plt.plot(ds['Frequency +10 10s']['Time'], ds['Frequency +10 10s']['Value'], color=colorsComp[1], linewidth=1)

plt.grid()
plt.title('Underfrequency Event +10MW')
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.legend(['H = 5s', 'H = 10s'], loc='upper right')
plt.savefig('plots/UnderfrequencyComparison.jpg', dpi=400)
