import uproot, os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'font.size': 22})

ttbar = uproot.open(f"{os.getcwd()}/../fr-ntuple-v3/ttbarIncl.root")["Nominal"]

def getCorr(x_str, y_str):
    x = ttbar.array(x_str)
    y = ttbar.array(y_str)

    x_min = np.min(x)
    x_max = np.max(x)

    y_min = np.min(y)
    y_max = np.max(y)

    x_bins = np.linspace(x_min, x_max, 10)
    y_bins = np.linspace(y_min, y_max, 10)

    fig, ax = plt.subplots(figsize =(10, 7))
    # Creating plot
    plt.hist2d(x, y, bins =[x_bins, y_bins], cmap = plt.cm.cividis)
    plt.title("")

    # Adding color bar
    plt.colorbar()

    ax.set_xlabel('dRbb')
    ax.set_ylabel('dRTauLep') 

    # show plot 
    plt.tight_layout()
    plt.savefig(f'plots/after/h2d_{x_str}_{y_str}.pdf')

    print(f"Pearson correlation coefficient {x_str} - {y_str}: \n{np.corrcoef(x, y)}")

getCorr("dRbb", "dRTauLep")
getCorr("ST", "dRTauLep")
getCorr("ST", "dRbb")
getCorr("n_jets", "ST")
