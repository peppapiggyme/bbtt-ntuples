import ROOT as R
import os
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

#rwt = AnaTTbarTrueFake(tauid=False, isOS=True)
#rwt = AnaTTbarTrueFake(tauid=False, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB < 150000. && mTW > 60000.")
rwt = AnaTTbarTrueFake(tauid=True, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB > 150000. && mTW > 150000.")

# overwrite the region tex expression
#rwt.regionTeX = "t#bar{t}-CR: Mbb>150, MTW>40, No #tau ID"
#rwt.regionTeX = "RW-VR1: Mbb<150, MTW>60, No #tau ID"
rwt.regionTeX = "RW-VR2: Mbb>150, MTW>150, Pass #tau ID"

#suffix_before = f"_os_CR_before.pdf"
#suffix_before = f"_os_VR1_before.pdf"
suffix_before = f"_os_VR2_before.pdf"

# apply reweighting
# -----------------
# print(f"{TermColor.OKBLUE}Applying norm to ttbar ... {TermColor.ENDC}")
# rwt.applyTauSFAndTTBarNorm("weight", "weight_norm")
rwt.applyTauSF("weight")

# print(f"{TermColor.OKBLUE}Applying reweight to ttbar ... {TermColor.ENDC}")
# rwt.applyTauSFAndTTBarNormAndWeightStep1("weight", "weight_rw", ("ST", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")))

# make plots
# ----------
print(f"{TermColor.OKBLUE}Preparing before plots ... {TermColor.ENDC}")
plotAllTTbarTrueFakePlot(rwt, "weight_new", "njets", suffix_before)

# print(f"{TermColor.OKBLUE}Preparing after normalisation plots ... {TermColor.ENDC}")
# plotAllTTbarTrueFakePlot(rwt, "weight_norm", "njets", suffix_before)

# print(f"{TermColor.OKBLUE}Preparing after reweighitng plots ... {TermColor.ENDC}")
# plotAllTTbarTrueFakePlot(rwt, "weight_rw", "njets", suffix_after)

print(f"{TermColor.OKGREEN}Plotting done! {TermColor.ENDC}")
