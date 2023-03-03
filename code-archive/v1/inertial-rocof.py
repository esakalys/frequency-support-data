import functions as f
import matplotlib.pyplot as plt

# Program used to plot the inertial rocof data
scenarios = ['+5MW', '+10MW', '+20MW']

colors = ['#279B00', '#0089BF', '#FC2525']
for scenario in scenarios:
  files = [f'rocof {scenario} 5s.mat',
           f'rocof {scenario} 10s.mat',
           f'rocof {scenario} 20s.mat']

  dsBase = f.importData(files[0], 'data/baselineMat', single=True)
  dsVsc = f.importData(files[1:3], 'data/inertialMat')

  plt.figure(figsize=(6, 4), dpi=400)

  plt.plot(dsVsc[files[2]]['Time'], dsVsc[files[2]]['Value'], color=colors[2], linewidth=2, label='With VSC - 20s')
  plt.plot(dsVsc[files[1]]['Time'], dsVsc[files[1]]['Value'], color=colors[1], linewidth=2, label='With VSC - 10s')
  plt.plot(dsBase[files[0]]['Time'], dsBase[files[0]]['Value'], color=colors[0], linestyle='--', linewidth=2, label='Without VSC')

  plt.grid()
  plt.title('VSC - Inertial Support - RoCoF')
  plt.xlabel('Time, s')
  plt.ylabel('RoCoF, Hz/s')
  plt.xlim([0, 35])
  plt.legend(loc='lower right')
  plt.savefig(f'reportPlots/inertialRocof({scenario}).jpg', dpi=400)
