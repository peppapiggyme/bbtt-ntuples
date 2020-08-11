import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

# FR-R
clos = AnaTTbarTrueFake(tauid=False, isOS=True)

print(f"{TermColor.OKBLUE}Applying to njets inclusive samples ... {TermColor.ENDC}")
clos.applyWeightStep1(("HT", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")), True)

print(f"{TermColor.OKBLUE}Applying second step reweighting ... {TermColor.ENDC}")
clos.applyWeightStep2(("dRbb", os.path.join(os.getcwd(), "include", f"Reweight1D_dRbb.h")), True)

print(f"{TermColor.OKBLUE}Applying third step reweighting ... {TermColor.ENDC}")
clos.applyWeightStep3(("dRTauLep", os.path.join(os.getcwd(), "include", f"Reweight1D_dRlh.h")), True)

# parametrisations
clos_tau_pt = TTbarTrueFakePlot(clos, "tau_pt", "weight_extra", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 70000, 100000, 1000000]))

# basically reweight again, but take the difference against 1 as uncertainty ...
reweight1D(clos_tau_pt, "#tau_{had} p_{T} [MeV]", f"plots/dRlh/clos_tau_pt_fr_os.pdf", "_clos_tau_pt", drawOpt="HIST")

# VR1
clos = AnaTTbarTrueFake(tauid=False, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB < 150000. && mTW > 60000.")

print(f"{TermColor.OKBLUE}Applying to njets inclusive samples ... {TermColor.ENDC}")
clos.applyWeightStep1(("HT", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")), False)

print(f"{TermColor.OKBLUE}Applying second step reweighting ... {TermColor.ENDC}")
clos.applyWeightStep2(("dRbb", os.path.join(os.getcwd(), "include", f"Reweight1D_dRbb.h")), False)

print(f"{TermColor.OKBLUE}Applying third step reweighting ... {TermColor.ENDC}")
clos.applyWeightStep3(("dRTauLep", os.path.join(os.getcwd(), "include", f"Reweight1D_dRlh.h")), False)

# parametrisations
binning_bb = [0, 0.6, 1, 1.5, 2, 2.5, 3, 10]
clos_dRbb = TTbarTrueFakePlot(clos, "dRbb", "weight_extra", (36, 0, 6), rebin=array.array('d', binning_bb))

# basically reweight again, but take the difference against 1 as uncertainty ...
reweight1D(clos_dRbb, "#DeltaR(b, b)", f"plots/dRlh/clos_dRbb_fr_os.pdf", "_clos_dRbb", drawOpt="HIST")
