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
clos.applyWeightStep1(("ST", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")), True)

print(f"{TermColor.OKBLUE}Applying second step reweighting ... {TermColor.ENDC}")
clos.applyWeightStep2(("dRbb", os.path.join(os.getcwd(), "include", f"Reweight1D_dRbb.h")), True)

print(f"{TermColor.OKBLUE}Applying third step reweighting ... {TermColor.ENDC}")
clos.applyWeightStep3(("dRTauLep", os.path.join(os.getcwd(), "include", f"Reweight1D_dRlh.h")), True)

# parametrisations
clos_tau_pt = TTbarTrueFakePlot(clos, "tau_pt", "weight_final", (980, 20000, 1000000), array.array(
    'd', [20000, 25000, 30000, 35000, 40000, 45000, 50000, 60000, 70000, 80000, 90000, 100000, 1000000]))
clos_mhh = TTbarTrueFakePlot(clos, "mHH", "weight_extra", (1800, 200000, 2000000), array.array(
    'd', [200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1200000, 2000000]))

# basically reweight again, but take the difference against 1 as uncertainty ...
reweight1D(clos_tau_pt, "#tau_{had} p_{T} [MeV]", f"plots/dRlh/clos_tau_pt_fr_os.pdf", "_clos_tau_pt", drawOpt="HIST")
reweight1D(clos_mhh, "#M_{HH} [MeV]", f"plots/dRlh/clos_mhh_fr_os.pdf", "_clos_mhh", drawOpt="HIST")
