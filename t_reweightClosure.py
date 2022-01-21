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
    clos.add_var("tau_pt_GeV", "tau_pt / 1e3")
    clos.add_var("ST_GeV", "ST / 1e3")

    print(f"{TermColor.OKBLUE}Applying to njets inclusive samples ... {TermColor.ENDC}")
    clos.applyTauSFAndTTBarNormAndWeightStep1("weight", "weight_rw", ("ST_GeV", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")))

    # parametrisations
    binning = [20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 90, 120, 160, 250, 500, 1000]
    clos_tau_pt = TTbarTrueFakePlot(clos, "tau_pt_GeV", "weight_rw", (980, 20, 1000), array.array('d',  binning))
    clos_tau_pt.checkYields()

    # basically reweight again, but take the difference against 1 as uncertainty ...
    reweight1D(clos_tau_pt, f"#tau_{{had}} p_{{T}} ({p}-prong) [GeV]", f"plots/njets/clos_tau_pt_fr_os_{p}p.pdf", f"_clos_tau_pt_{p}p", 
        drawOpt="HIST", rel=True, canvas_size=(1200,900), ytitle="Relative Uncertainty", yrange=(-0.2, 0.2), hline=0)
