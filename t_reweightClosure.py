import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

for p in [1, 3]:
    # FR-R
    clos = AnaTTbarTrueFake(tauid=False, isOS=True, prong=p)

    print(f"{TermColor.OKBLUE}Applying to njets inclusive samples ... {TermColor.ENDC}")
    clos.applyTauSFAndTTBarNormAndWeightStep1("weight", "weight_rw", ("ST", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")))

    # parametrisations
    binning = [20000, 25000, 30000, 35000, 40000, 45000, 50000, 
        55000, 60000, 70000, 90000, 120000, 160000, 250000, 500000, 1000000]
    clos_tau_pt = TTbarTrueFakePlot(clos, "tau_pt", "weight_rw", (980, 20000, 1000000), array.array('d',  binning))

    # basically reweight again, but take the difference against 1 as uncertainty ...
    reweight1D(clos_tau_pt, "#tau_{had} p_{T} [MeV]", f"plots/njets/clos_tau_pt_fr_os_{p}p.pdf", f"_clos_tau_pt_{p}p", drawOpt="HIST")
