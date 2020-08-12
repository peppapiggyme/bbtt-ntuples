import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

print(f"{TermColor.OKBLUE}Starting program ... {TermColor.ENDC}")

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

rwt = AnaTTbarTrueFake(tauid=False, isOS=True)

regionTeX = "lephad, OS, Mbb sideband (50~100, 150~350), MTW>40, No #tau ID"

df_njets = {}
for i in range(2, 11):
    df_njets[i] = {}

for p in rwt.processes:
    for i in range(2, 10):
        df_njets[i][p] = rwt.df[p].Filter("n_jets == " + str(i))
    df_njets[10][p] = rwt.df[p].Filter("n_jets >= 10")

print(f"{TermColor.OKBLUE}Start reweighting ... {TermColor.ENDC}")

for i in range(2, 11):
    print(f"{TermColor.BOLD}Analyzing number of jets = {i} (if i = 10, means #jets >= 10){TermColor.ENDC}")

    rwt.set_current_df(df_njets[i])

    # Before reweighting
    # ------------------

    suffix_before = f"_before.pdf"

    binning_st = {}
    binning_st[2] = [50000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 600000, 750000, 3000000]
    binning_st[3] = [50000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 600000, 750000, 3000000]
    binning_st[4] = [50000, 250000, 300000, 350000, 400000, 450000, 500000, 600000, 700000, 750000, 900000, 3000000]
    binning_st[5] = [50000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 900000, 1000000, 3000000]
    binning_st[6] = [50000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 900000, 1000000, 3000000]
    binning_st[7] = [50000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1200000, 1500000, 3000000]
    binning_st[8] = [50000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1200000, 1500000, 3000000]
    binning_st[9] = [50000, 500000, 700000, 900000, 1200000, 1500000, 3000000]
    binning_st[10] = [50000, 700000, 1000000, 1200000, 1500000, 3000000]

    # rwt_ht = TTbarTrueFakePlot(rwt, "HT", "weight", (3000, 0, 3000000), array.array('d', binning_st[i]))
    # drawStack(rwt_ht, "H_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_ht_fr_os" + suffix_before)

    rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight", (3000, 0, 3000000), array.array('d', binning_st[i]))
    drawStack(rwt_st, "S_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_st_fr_os" + suffix_before)

    # rwt_njets = TTbarTrueFakePlot(rwt, "n_jets", "weight", (11, 2, 13))
    # drawStack(rwt_njets, "# jets", regionTeX, f"plots/{i}jets/stack_njets_fr_os" + suffix_before)
    
    print(f"{TermColor.OKBLUE}Yields (Before reweighting) {TermColor.ENDC}")
    
    rwt_st.checkYields()

    reweight1D(rwt_st, "S_{T} [MeV]", f"plots/{i}jets/wt1d_st_fr_os.pdf", f"_{i}jets")

    # Apply reweighting
    # ------------------

    rwt.applyWeightNjets(("ST", os.path.join(os.getcwd(), "include", f"Reweight1D_{i}jets.h")), f"_{i}jets")

    # After reweighting
    # ------------------

    suffix_after = f"_after.pdf"

    rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight_new", (2000, 0, 2000000), array.array(
        'd', [i for i in range(0, 2050000, 50000)]))
    drawStack(rwt_st, "S_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_st_fr_os" + suffix_after)

    rwt_njets = TTbarTrueFakePlot(rwt, "n_jets", "weight_new", (11, 2, 13))
    drawStack(rwt_njets, "# jets", regionTeX, f"plots/{i}jets/stack_njets_fr_os" + suffix_after)

    print(f"{TermColor.OKBLUE}Yields (After reweighting) {TermColor.ENDC}")

    rwt_st.checkYields()

    print(f"{TermColor.OKGREEN}Finished njets = {i}! {TermColor.ENDC}")

print(f"{TermColor.OKGREEN}All n jets are done! {TermColor.ENDC}")
del rwt

rwt = AnaTTbarTrueFake(tauid=False, isOS=True)

rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight", (2000, 0, 2000000))
print(f"{TermColor.OKBLUE}Yields (Before reweighting) {TermColor.ENDC}")
rwt_st.checkYields()

rwt.applyWeightStep1(("ST", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")), False)

rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight_new", (2000, 0, 2000000))
print(f"{TermColor.OKBLUE}Yields (After reweighting step 1) {TermColor.ENDC}")
rwt_st.checkYields()

# step 2 reweighting
# ------------------
print(f"{TermColor.OKBLUE}Second step reweighting with dRbb {TermColor.ENDC}")

binning_bb = [0, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 10]
rwt_dr_bb = TTbarTrueFakePlot(rwt, "dRbb", "weight_new", (12, 0, 6), rebin=array.array('d', binning_bb))
reweight1D(rwt_dr_bb, "#DeltaR(b, b)", f"plots/dRbb/wt1d_dRbb_fr_os.pdf", f"_dRbb")

rwt.applyWeightStep2(("dRbb", os.path.join(os.getcwd(), "include", f"Reweight1D_dRbb.h")), True)
rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight_final", (2000, 0, 2000000))
print(f"{TermColor.OKBLUE}Yields (After reweighting step 2) {TermColor.ENDC}")
rwt_st.checkYields()

# # step 3 reweighting
# # ------------------
# print(f"{TermColor.OKBLUE}Third step reweighting with dRTauLep {TermColor.ENDC}")

# binning_lh = [0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 10]
# rwt_dr_lh = TTbarTrueFakePlot(rwt, "dRTauLep", "weight_final", (12, 0, 6), rebin=array.array('d', binning_lh))
# reweight1D(rwt_dr_lh, "#DeltaR(lep, #tau)", f"plots/dRlh/wt1d_dRlh_fr_os.pdf", f"_dRlh")

# rwt.applyWeightStep3(("dRTauLep", os.path.join(os.getcwd(), "include", f"Reweight1D_dRlh.h")), True)
# rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight_extra", (2000, 0, 2000000))
# print(f"{TermColor.OKBLUE}Yields (After reweighting step 3) {TermColor.ENDC}")
# rwt_st.checkYields()
