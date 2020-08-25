import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

#rwt = AnaTTbarTrueFake(tauid=True, isOS=True)
rwt = AnaTTbarTrueFake(tauid=True, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 150000.")

#regionTeX = "lephad, OS, Mbb sideband, MTW>40, Pass #tau ID"
regionTeX = "lephad, OS, Mbb sideband, MTW>150, Pass #tau ID"

suffix_before = f"_tauid_before.pdf"
suffix_after  = f"_tauid_after.pdf"
suffix_final  = f"_tauid_final.pdf"
suffix_extra  = f"_tauid_extra.pdf"

print(f"{TermColor.OKBLUE}Preparing before reweighitng plots ... {TermColor.ENDC}")

rwt_plot = TTbarTrueFakePlot(rwt, "MET", "weight", (400, 0, 400000), array.array(
    'd', [i for i in range(0, 420000, 20000)]))
drawStack(rwt_plot, "MET [MeV]", regionTeX, f"plots/njets/stack_met_fr_os" + suffix_before)
rwt_plot.checkYields()

rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "weight", (36, 20000, 200000))
drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/njets/stack_lep_ptlow_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "weight", (36, 20000, 200000))
drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/njets/stack_tau_ptlow_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "weight", (40, 50000, 250000))
drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b0_ptlow_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "weight", (36, 20000, 200000))
drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b1_ptlow_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "weight", (380, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/njets/stack_lep_pt_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "weight", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/njets/stack_tau_pt_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "weight", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b0_pt_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "weight", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b1_pt_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "mTW", "weight", (40, 40000, 240000))
drawStack(rwt_plot, "M_{T} [MeV]", regionTeX, f"plots/njets/stack_mtw_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "mBB", "weight", (40, 0, 400000))
drawStack(rwt_plot, "Mbb [MeV]", regionTeX, f"plots/njets/stack_mbb_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "mHH", "weight", (40, 200000, 2200000))
drawStack(rwt_plot, "Mhh [MeV]", regionTeX, f"plots/njets/stack_mhh_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "HT", "weight", (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot, "H_{T} [MeV]", regionTeX, f"plots/njets/stack_ht_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "ST", "weight", (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot, "S_{T} [MeV]", regionTeX, f"plots/njets/stack_st_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "n_jets", "weight", (11, 2, 13))
drawStack(rwt_plot, "# jets", regionTeX, f"plots/njets/stack_njets_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "lead_jet_pt", "weight", (50, 50000, 550000))
drawStack(rwt_plot, "leading jet pT [MeV]", regionTeX, f"plots/njets/stack_lead_jet_ptlow_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "dRTauLep", "weight", (36, 0, 6))
drawStack(rwt_plot, "#DeltaR(lep, #tau)", regionTeX, f"plots/njets/stack_dr_lep_tau_fr_os" + suffix_before)

rwt_plot = TTbarTrueFakePlot(rwt, "dRbb", "weight", (36, 0, 6))
drawStack(rwt_plot, "#DeltaR(b, b)", regionTeX, f"plots/njets/stack_dr_bb_fr_os" + suffix_before)

print(f"{TermColor.OKGREEN}Plotting done! {TermColor.ENDC}")

print(f"{TermColor.OKBLUE}Yields (Before reweighting) {TermColor.ENDC}")

rwt_plot.checkYields()

# apply reweighting
# -----------------

print(f"{TermColor.OKBLUE}Applying to njets inclusive samples ... {TermColor.ENDC}")
rwt.applyWeightStep1(("ST", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")), True)

# after reweighting
# -----------------

rwt.set_current_df(rwt.df)

print(f"{TermColor.OKBLUE}Preparing after reweighitng plots ... {TermColor.ENDC}")

rwt_plot = TTbarTrueFakePlot(rwt, "MET", "weight_new", (400, 0, 400000), array.array(
    'd', [i for i in range(0, 420000, 20000)]))
drawStack(rwt_plot, "MET [MeV]", regionTeX, f"plots/njets/stack_met_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "weight_new", (36, 20000, 200000))
drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/njets/stack_lep_ptlow_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "weight_new", (36, 20000, 200000))
drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/njets/stack_tau_ptlow_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "weight_new", (40, 50000, 250000))
drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b0_ptlow_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "weight_new", (36, 20000, 200000))
drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b1_ptlow_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "weight_new", (380, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/njets/stack_lep_pt_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "weight_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/njets/stack_tau_pt_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "weight_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b0_pt_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "weight_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/njets/stack_b1_pt_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "mTW", "weight_new", (40, 40000, 240000))
drawStack(rwt_plot, "M_{T} [MeV]", regionTeX, f"plots/njets/stack_mtw_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "mBB", "weight_new", (40, 0, 400000))
drawStack(rwt_plot, "Mbb [MeV]", regionTeX, f"plots/njets/stack_mbb_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "mHH", "weight_new", (40, 200000, 2200000))
drawStack(rwt_plot, "Mhh [MeV]", regionTeX, f"plots/njets/stack_mhh_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "HT", "weight_new", (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot, "H_{T} [MeV]", regionTeX, f"plots/njets/stack_ht_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "ST", "weight_new", (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot, "S_{T} [MeV]", regionTeX, f"plots/njets/stack_st_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "n_jets", "weight_new", (11, 2, 13))
drawStack(rwt_plot, "# jets", regionTeX, f"plots/njets/stack_njets_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "lead_jet_pt", "weight_new", (50, 50000, 550000))
drawStack(rwt_plot, "leading jet pT [MeV]", regionTeX, f"plots/njets/stack_lead_jet_ptlow_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "dRTauLep", "weight_new", (36, 0, 6))
drawStack(rwt_plot, "#DeltaR(lep, #tau)", regionTeX, f"plots/njets/stack_dr_lep_tau_fr_os" + suffix_after)

rwt_plot = TTbarTrueFakePlot(rwt, "dRbb", "weight_new", (36, 0, 6))
drawStack(rwt_plot, "#DeltaR(b, b)", regionTeX, f"plots/njets/stack_dr_bb_fr_os" + suffix_after)

print(f"{TermColor.OKBLUE}Yields (After reweighting) {TermColor.ENDC}")

rwt_plot.checkYields()

# (new!) step 2 reweighting
# -------------------------
print(f"{TermColor.OKBLUE}Applying second step reweighting ... {TermColor.ENDC}")
rwt.applyWeightStep2(("dRbb", os.path.join(os.getcwd(), "include", f"Reweight1D_dRbb.h")), True)

print(f"{TermColor.OKBLUE}Preparing after 2nd reweighitng plots ... {TermColor.ENDC}")

rwt_plot = TTbarTrueFakePlot(rwt, "MET", "weight_final", (400, 0, 400000), array.array(
    'd', [i for i in range(0, 420000, 20000)]))
drawStack(rwt_plot, "MET [MeV]", regionTeX, f"plots/dRbb/stack_met_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "weight_final", (36, 20000, 200000))
drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/dRbb/stack_lep_ptlow_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "weight_final", (36, 20000, 200000))
drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/dRbb/stack_tau_ptlow_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "weight_final", (40, 50000, 250000))
drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/dRbb/stack_b0_ptlow_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "weight_final", (36, 20000, 200000))
drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/dRbb/stack_b1_ptlow_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "weight_final", (380, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/dRbb/stack_lep_pt_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "weight_final", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/dRbb/stack_tau_pt_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "weight_final", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/dRbb/stack_b0_pt_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "weight_final", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/dRbb/stack_b1_pt_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "mTW", "weight_final", (40, 40000, 240000))
drawStack(rwt_plot, "M_{T} [MeV]", regionTeX, f"plots/dRbb/stack_mtw_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "mBB", "weight_final", (40, 0, 400000))
drawStack(rwt_plot, "Mbb [MeV]", regionTeX, f"plots/dRbb/stack_mbb_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "mHH", "weight_final", (40, 200000, 2200000))
drawStack(rwt_plot, "Mhh [MeV]", regionTeX, f"plots/dRbb/stack_mhh_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "HT", "weight_final", (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot, "H_{T} [MeV]", regionTeX, f"plots/dRbb/stack_ht_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "ST", "weight_final", (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot, "S_{T} [MeV]", regionTeX, f"plots/dRbb/stack_st_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "n_jets", "weight_final", (11, 2, 13))
drawStack(rwt_plot, "# jets", regionTeX, f"plots/dRbb/stack_njets_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "lead_jet_pt", "weight_final", (50, 50000, 550000))
drawStack(rwt_plot, "leading jet pT [MeV]", regionTeX, f"plots/dRbb/stack_lead_jet_ptlow_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "dRTauLep", "weight_final", (36, 0, 6))
drawStack(rwt_plot, "#DeltaR(lep, #tau)", regionTeX, f"plots/dRbb/stack_dr_lep_tau_fr_os" + suffix_final)

rwt_plot = TTbarTrueFakePlot(rwt, "dRbb", "weight_final", (36, 0, 6))
drawStack(rwt_plot, "#DeltaR(b, b)", regionTeX, f"plots/dRbb/stack_dr_bb_fr_os" + suffix_final)

rwt_plot.checkYields()

print(f"{TermColor.OKGREEN}Plotting done! {TermColor.ENDC}")

# (new!) step 3 reweighting
# -------------------------
print(f"{TermColor.OKBLUE}Applying third step reweighting ... {TermColor.ENDC}")
rwt.applyWeightStep3(("dRTauLep", os.path.join(os.getcwd(), "include", f"Reweight1D_dRlh.h")), True)

print(f"{TermColor.OKBLUE}Preparing after 3rd reweighitng plots ... {TermColor.ENDC}")

rwt_plot = TTbarTrueFakePlot(rwt, "MET", "weight_extra", (400, 0, 400000), array.array(
    'd', [i for i in range(0, 420000, 20000)]))
drawStack(rwt_plot, "MET [MeV]", regionTeX, f"plots/dRlh/stack_met_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "weight_extra", (36, 20000, 200000))
drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/dRlh/stack_lep_ptlow_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "weight_extra", (36, 20000, 200000))
drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/dRlh/stack_tau_ptlow_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "weight_extra", (40, 50000, 250000))
drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/dRlh/stack_b0_ptlow_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "weight_extra", (36, 20000, 200000))
drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/dRlh/stack_b1_ptlow_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "weight_extra", (380, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/dRlh/stack_lep_pt_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "weight_extra", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/dRlh/stack_tau_pt_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "weight_extra", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/dRlh/stack_b0_pt_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "weight_extra", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/dRlh/stack_b1_pt_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "mTW", "weight_extra", (40, 40000, 240000))
drawStack(rwt_plot, "M_{T} [MeV]", regionTeX, f"plots/dRlh/stack_mtw_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "mBB", "weight_extra", (40, 0, 400000))
drawStack(rwt_plot, "Mbb [MeV]", regionTeX, f"plots/dRlh/stack_mbb_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "mHH", "weight_extra", (40, 200000, 2200000))
drawStack(rwt_plot, "Mhh [MeV]", regionTeX, f"plots/dRlh/stack_mhh_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "HT", "weight_extra", (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot, "H_{T} [MeV]", regionTeX, f"plots/dRlh/stack_ht_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "ST", "weight_extra", (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot, "S_{T} [MeV]", regionTeX, f"plots/dRlh/stack_st_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "n_jets", "weight_extra", (11, 2, 13))
drawStack(rwt_plot, "# jets", regionTeX, f"plots/dRlh/stack_njets_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "lead_jet_pt", "weight_extra", (50, 50000, 550000))
drawStack(rwt_plot, "leading jet pT [MeV]", regionTeX, f"plots/dRlh/stack_lead_jet_ptlow_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "dRTauLep", "weight_extra", (36, 0, 6))
drawStack(rwt_plot, "#DeltaR(lep, #tau)", regionTeX, f"plots/dRlh/stack_dr_lep_tau_fr_os" + suffix_extra)

rwt_plot = TTbarTrueFakePlot(rwt, "dRbb", "weight_extra", (36, 0, 6))
drawStack(rwt_plot, "#DeltaR(b, b)", regionTeX, f"plots/dRlh/stack_dr_bb_fr_os" + suffix_extra)

rwt_plot.checkYields()

print(f"{TermColor.OKGREEN}Plotting done! {TermColor.ENDC}")