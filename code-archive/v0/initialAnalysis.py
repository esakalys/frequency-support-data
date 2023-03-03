
import matplotlib.pyplot as plt
import os
import functions as f

# Program to plot initial exploratory simulation data

dir = os.getcwd()
files = os.listdir(f'{dir}/data/matFiles')

ds = f.importData(files, 'data/matFiles', trimTime=False)

colorsBlue = ["#0A2136","#133557","#1C4977","#265E98","#2F72B9","#3886D9","#419AFA"]
colorsRed = ["#751414","#8B1D1D","#A12626","#B83030","#CE3939","#E44242","#FA4B4B"]
colorsComp = ["#409823","#E47928"]

# Sorting the data by simulated event

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

# Sorting the data to make sure everything is in the right order
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

# H = 5s Underfrequency events - Frequency
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
plt.savefig('initialPlots/UnderfrequencyEventsF5s.jpg', dpi=400)

# H = 5s Underfrequency events - Power
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
plt.savefig('initialPlots/UnderfrequencyEventsP5s.jpg', dpi=400)

# H = 5s Overfrequency events - Frequency
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
plt.savefig('initialPlots/OverfrequencyEventsF5s.jpg', dpi=400)

# H = 5s Overfrequency events - Power
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
plt.savefig('initialPlots/OverfrequencyEventsP5s.jpg', dpi=400)

# H = 10s Underfrequency events - Frequency
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
plt.savefig('initialPlots/UnderfrequencyEventsF10s.jpg', dpi=400)

# H = 10s Underfrequency events - Power
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
plt.savefig('initialPlots/UnderfrequencyEventsP10s.jpg', dpi=400)

# H = 10s Overfrequency events - Frequency
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
plt.savefig('initialPlots/OverfrequencyEventsF10s.jpg', dpi=400)

# H = 10s Overfrequency events - Power
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
plt.savefig('initialPlots/OverfrequencyEventsP10s.jpg', dpi=400)

# Comparisons between H = 5s and H = 10s
# -10 MW
plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds['Frequency -10 5s']['Time'], ds['Frequency -10 5s']['Value'], color=colorsComp[0], linewidth=1)
plt.plot(ds['Frequency -10 10s']['Time'], ds['Frequency -10 10s']['Value'], color=colorsComp[1], linewidth=1)

plt.grid()
plt.title('Overfrequency Event -10MW')
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.legend(['H = 5s', 'H = 10s'], loc='upper right')
plt.savefig('initialPlots/OverfrequencyComparison.jpg', dpi=400)

# +10 MW
plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds['Frequency +10 5s']['Time'], ds['Frequency +10 5s']['Value'], color=colorsComp[0], linewidth=1)
plt.plot(ds['Frequency +10 10s']['Time'], ds['Frequency +10 10s']['Value'], color=colorsComp[1], linewidth=1)

plt.grid()
plt.title('Underfrequency Event +10MW')
plt.xlabel('Time, s')
plt.ylabel('Frequency, Hz')
plt.legend(['H = 5s', 'H = 10s'], loc='upper right')
plt.savefig('initialPlots/UnderfrequencyComparison.jpg', dpi=400)
