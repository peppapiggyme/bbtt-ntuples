import os
import ROOT as R
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

rwt = AnaTTbarTrueFake(tauid=False, isOS=True, path=f"{os.getcwd()}/../fr-ntuple-v14/", rewrite="n_btag == 2 && n_jets >= 2")

regionTeX = "lephad, OS, no ID"

suffix_before = f"_before.pdf"
 
print(f"{TermColor.OKBLUE}Preparing before reweighitng plots ... {TermColor.ENDC}")

rwt_plot = TTbarTrueFakePlot(rwt, "MET", "weight", (40, 0, 400000))
rwt_plot.checkYields()
drawStack(rwt_plot, "MET [MeV]", regionTeX, f"plots/njets/stack_met_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "mTW", "weight", (40, 0, 400000))
drawStack(rwt_plot, "M_{T} [MeV]", regionTeX, f"plots/njets/stack_mtw_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "mBB", "weight", (40, 0, 400000))
drawStack(rwt_plot, "Mbb [MeV]", regionTeX, f"plots/njets/stack_mbb_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "weight", (38, 20000, 400000))
drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/njets/stack_lep_ptlow_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "weight", (38, 20000, 400000))
drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/njets/stack_tau_ptlow_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "weight", (40, 50000, 250000))
# drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b0_ptlow_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "weight", (36, 20000, 200000))
# drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b1_ptlow_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "weight", (380, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/njets/stack_lep_pt_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "weight", (980, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/njets/stack_tau_pt_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "weight", (980, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b0_pt_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "weight", (980, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b1_pt_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "mHH", "weight", (40, 200000, 2200000))
# drawStack(rwt_plot, "Mhh [MeV]", regionTeX, f"plots/njets/stack_mhh_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "HT", "weight", (2000, 0, 2000000), array.array(
#     'd', [i for i in range(0, 2050000, 50000)]))
# drawStack(rwt_plot, "H_{T} [MeV]", regionTeX, f"plots/njets/stack_ht_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "ST", "weight", (2000, 0, 2000000), array.array(
#     'd', [i for i in range(0, 2050000, 50000)]))
# drawStack(rwt_plot, "S_{T} [MeV]", regionTeX, f"plots/njets/stack_st_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "n_jets", "weight", (11, 2, 13))
# drawStack(rwt_plot, "# jets", regionTeX, f"plots/njets/stack_njets_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "lead_jet_pt", "weight", (50, 50000, 550000))
# drawStack(rwt_plot, "leading jet pT [MeV]", regionTeX, f"plots/njets/stack_lead_jet_ptlow_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "dRTauLep", "weight", (36, 0, 6))
# drawStack(rwt_plot, "#DeltaR(lep, #tau)", regionTeX, f"plots/njets/stack_dr_lep_tau_fr_os" + suffix_before)

# rwt_plot = TTbarTrueFakePlot(rwt, "dRbb", "weight", (36, 0, 6))
# drawStack(rwt_plot, "#DeltaR(b, b)", regionTeX, f"plots/njets/stack_dr_bb_fr_os" + suffix_before)

print(f"{TermColor.OKGREEN}Plotting done! {TermColor.ENDC}")

print(f"{TermColor.OKBLUE}Yields (Before reweighting) {TermColor.ENDC}")
