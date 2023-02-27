import functions as f
import matplotlib.pyplot as plt

# Program used to plot the droop power data
scenarios = ['+5MW', '+10MW', '+20MW']
coefficients = ['1', '2']

colors = ['#279B00', '#0089BF', '#FC2525']
for scenario in scenarios:
  for c in coefficients:
    files = [f'PowerGen {scenario} 5s.mat',
            f'PowerGen {scenario} {c}.mat',
            f'PowerVsc {scenario} {c}.mat']

    dsBase = f.importData(files[0], 'data/baselineMat', single=True)
    dsGen = f.importData(files[1], 'data/droopMat', single=True)
    dsVsc = f.importData(files[2], 'data/droopMat', single=True)

    # Generator Power Output
    plt.figure(figsize=(6, 4), dpi=400)

    plt.plot(dsGen[files[1]]['Time'], dsGen[files[1]]['Value'], color=colors[1], linewidth=1, label='With VSC')
    plt.plot(dsBase[files[0]]['Time'], dsBase[files[0]]['Value'], color=colors[0], linewidth=2, label='Without VSC')

    plt.grid()
    plt.title(f'VSC - Droop Support - Generator Power - Droop = {c}')
    plt.xlabel('Time, s')
    plt.ylabel('Power, MW')
    plt.xlim([0, 35])
    plt.ylim([30, 80])
    plt.legend(loc='lower right')
    plt.savefig(f'reportPlots/droopPowerGen({scenario}{c}).jpg', dpi=400)

    # VSC Power Output
    plt.figure(figsize=(6, 4), dpi=400)

    plt.plot(dsVsc[files[2]]['Time'], dsVsc[files[2]]['Value'], color=colors[2], linewidth=1)

    plt.grid()
    plt.title(f'VSC - Inertial Support - VSC Power - Droop = {c}')
    plt.xlabel('Time, s')
    plt.ylabel('Power, MW')
    plt.xlim([0, 35])
    plt.ylim([-5, 20])
    plt.savefig(f'reportPlots/droopPowerVSC({scenario}{c}).jpg', dpi=400)
