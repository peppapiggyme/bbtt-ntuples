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
clos_met = TTbarTrueFakePlot(clos, "MET", "weight_extra", (400, 0, 400000), array.array(
    'd', [20000, 40000, 60000, 80000, 100000, 120000, 160000, 220000, 300000, 400000]))

# basically reweight again, but take the difference against 1 as uncertainty ...
reweight1D(clos_tau_pt, "#tau_{had} p_{T} [MeV]", f"plots/dRlh/clos_tau_pt_fr_os.pdf", "_tau_pt")
reweight1D(clos_met, "MET [MeV]", f"plots/dRlh/clos_met_fr_os.pdf", "_met")

# VR1
clos = AnaTTbarTrueFake(tauid=False, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB < 150000. && mTW > 60000.")

print(f"{TermColor.OKBLUE}Applying to njets inclusive samples ... {TermColor.ENDC}")
clos.applyWeightStep1(("HT", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")), True)

print(f"{TermColor.OKBLUE}Applying second step reweighting ... {TermColor.ENDC}")
clos.applyWeightStep2(("dRbb", os.path.join(os.getcwd(), "include", f"Reweight1D_dRbb.h")), True)

print(f"{TermColor.OKBLUE}Applying third step reweighting ... {TermColor.ENDC}")
clos.applyWeightStep3(("dRTauLep", os.path.join(os.getcwd(), "include", f"Reweight1D_dRlh.h")), True)

# parametrisations
clos_mhh = TTbarTrueFakePlot(clos, "mHH", "weight_extra", (2000, 200000, 2200000), array.array(
    'd', [200000, 350000, 450000, 500000, 550000, 600000, 700000, 800000, 900000, 1200000, 2200000]))

# basically reweight again, but take the difference against 1 as uncertainty ...
reweight1D(clos_tau_pt, "#M_{HH} [MeV]", f"plots/dRlh/clos_mhh_fr_os.pdf", "_mhh")
