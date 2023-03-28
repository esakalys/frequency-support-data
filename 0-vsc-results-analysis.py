import functions as f
import matplotlib.pyplot as plt

# Program used to plot the general VSC control results

iqFiles = ['iq.mat', 'iqRef.mat']
idFiles = ['id.mat', 'idRef.mat']
vscPowerFiles = ['power-vsc.mat', 'power-vsc-ref.mat']
vsc = ['vVsc.mat', 'iVsc.mat']


time = [4.5, 5.5]

# Plotting q current
ds = f.importData(iqFiles, 'data/v2-data/0-vsc-results-unfiltered')

plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds[iqFiles[0]]['Time'], ds[iqFiles[0]]['Value'],
         color='#0789FA', linewidth=1.4, label='q Current')
plt.plot(ds[iqFiles[1]]['Time'], ds[iqFiles[1]]['Value'],
         color='#F10A0A', linewidth=1.4, label='q Current Reference', linestyle='--')

plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
plt.title('VSC Results - q Current', pad=20)
plt.xlabel('Time, s')
plt.ylabel('Current, A')
plt.xlim(time)
plt.ylim([-400, 400])
plt.legend(loc='lower right')
plt.savefig('plots/v2-plots/0-vsc-iq.jpg', dpi=400, bbox_inches='tight')

# Plotting d current
ds = f.importData(idFiles, 'data/v2-data/0-vsc-results-unfiltered')

plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds[idFiles[0]]['Time'], ds[idFiles[0]]['Value'],
         color='#0789FA', linewidth=1.4, label='d Current')
plt.plot(ds[idFiles[1]]['Time'], ds[idFiles[1]]['Value'],
         color='#F10A0A', linewidth=1.4, label='d Current Reference', linestyle='--')

plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
plt.title('VSC Results - d Current', pad=20)
plt.xlabel('Time, s')
plt.ylabel('Current, A')
plt.xlim(time)
plt.ylim([-1000, 0])
plt.legend(loc='upper right')
plt.savefig('plots/v2-plots/0-vsc-id.jpg', dpi=400, bbox_inches='tight')


# Plotting power
ds = f.importData(vscPowerFiles, 'data/v2-data/0-vsc-results-unfiltered')

plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds[vscPowerFiles[0]]['Time'], ds[vscPowerFiles[0]]['Value'],
         color='#0789FA', linewidth=1.4, label='VSC Power')
plt.plot(ds[vscPowerFiles[1]]['Time'], ds[vscPowerFiles[1]]['Value'],
         color='#F10A0A', linewidth=1.4, label='VSC Power Reference', linestyle='--')

plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
plt.title('VSC Results - Power', pad=20)
plt.xlabel('Time, s')
plt.ylabel('Power, MW')
plt.xlim(time)
plt.ylim([0, 30])
plt.legend(loc='lower right')
plt.savefig('plots/v2-plots/0-vsc-power.jpg', dpi=400, bbox_inches='tight')

phase_colors = ['#E60B09', '#34C62C', '#2C67C7']
phase_time = [4.9, 5.1]

# Plotting VSC Voltage
ds = f.import3phData(vsc, 'data/v2-data/0-vsc-results-unfiltered')

plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds[vsc[0]]['Time'], ds[vsc[0]]['a'],
         color=phase_colors[0], linewidth=1.4)
plt.plot(ds[vsc[0]]['Time'], ds[vsc[0]]['b'],
         color=phase_colors[1], linewidth=1.4)
plt.plot(ds[vsc[0]]['Time'], ds[vsc[0]]['c'],
         color=phase_colors[2], linewidth=1.4)

plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
plt.title('VSC Results - Voltage', pad=20)
plt.xlabel('Time, s')
plt.ylabel('Voltage, V')
plt.xlim(phase_time)
plt.ylim([-20000, 20000])
plt.savefig('plots/v2-plots/0-vsc-voltage.jpg', dpi=400, bbox_inches='tight')

# Plotting VSC Current
ds = f.import3phData(vsc, 'data/v2-data/0-vsc-results-unfiltered')

plt.figure(figsize=(6, 4), dpi=400)

plt.plot(ds[vsc[1]]['Time'], ds[vsc[1]]['a'],
         color=phase_colors[0], linewidth=1.4)
plt.plot(ds[vsc[1]]['Time'], ds[vsc[1]]['b'],
         color=phase_colors[1], linewidth=1.4)
plt.plot(ds[vsc[1]]['Time'], ds[vsc[1]]['c'],
         color=phase_colors[2], linewidth=1.4)

plt.grid(linewidth=0.3, linestyle='--', color='#E1E1E1')
plt.title('VSC Results - Current', pad=20)
plt.xlabel('Time, s')
plt.ylabel('Current, A')
plt.xlim(phase_time)
plt.ylim([-1000, 1000])
plt.savefig('plots/v2-plots/0-vsc-current.jpg', dpi=400, bbox_inches='tight')
