import functions as f
import matplotlib.pyplot as plt

# Program used to plot the droop + inertial power data
scenarios = ['-5MW', '-10MW', '-20MW']

colors = ['#279B00', '#0089BF', '#FC2525']
for scenario in scenarios:
  files = [f'PowerGen {scenario} 5s.mat',
          f'PowerGen {scenario}.mat',
          f'PowerVsc {scenario}.mat']

  dsBase = f.importData(files[0], 'data/baselineMat', single=True)
  dsGen = f.importData(files[1], 'data/ofMat', single=True)
  dsVsc = f.importData(files[2], 'data/ofMat', single=True)

  # Generator Power Output
  plt.figure(figsize=(6, 4), dpi=400)

  plt.plot(dsGen[files[1]]['Time'], dsGen[files[1]]['Value'], color=colors[1], linewidth=1, label='With VSC')
  plt.plot(dsBase[files[0]]['Time'], dsBase[files[0]]['Value'], color=colors[0], linewidth=2, label='Without VSC')

  plt.grid()
  plt.title(f'VSC - Droop & Inertial Support - Overfrequency - Generator Power')
  plt.xlabel('Time, s')
  plt.ylabel('Power, MW')
  plt.xlim([0, 35])
  plt.ylim([25, 55])
  plt.legend(loc='lower right')
  plt.savefig(f'reportPlots/ofPowerGen({scenario}).jpg', dpi=400)

  # VSC Power Output
  plt.figure(figsize=(6, 4), dpi=400)

  plt.plot(dsVsc[files[2]]['Time'], dsVsc[files[2]]['Value'], color=colors[2], linewidth=1)

  plt.grid()
  plt.title(f'VSC - Inertial Support - Overfrequency - VSC Power')
  plt.xlabel('Time, s')
  plt.ylabel('Power, MW')
  plt.xlim([0, 35])
  plt.ylim([-20, 5])
  plt.savefig(f'reportPlots/ofPowerVSC({scenario}).jpg', dpi=400)
