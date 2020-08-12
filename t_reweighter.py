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

suffix_before = f"_before.pdf"
suffix_after = f"_after.pdf"
suffix_final = f"_final.pdf"

df_njets = {}
for i in range(2, 11):
    df_njets[i] = {}

for p in rwt.processes:
    for i in range(2, 10):
        df_njets[i][p] = rwt.df[p].Filter("n_jets == " + str(i))
    df_njets[10][p] = rwt.df[p].Filter("n_jets >= 10")

print(f"{TermColor.OKBLUE}Start reweighting ... {TermColor.ENDC}")

# for i in range(2, 11):
#     print(f"{TermColor.BOLD}Analyzing number of jets = {i} (if i = 10, means #jets >= 10){TermColor.ENDC}")

#     rwt.set_current_df(df_njets[i])

#     # Before reweighting
#     # ------------------

#     binning_st = {}
#     binning_st[2] = [0, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 600000, 700000, 3000000]
#     binning_st[3] = [0, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 600000, 700000, 800000, 3000000]
#     binning_st[4] = [0, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 700000, 800000, 900000, 3000000]
#     binning_st[5] = [0, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 700000, 800000, 900000, 1000000, 3000000]
#     binning_st[6] = [0, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 800000, 900000, 1000000, 3000000]
#     binning_st[7] = [0, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1200000, 1400000, 3000000]
#     binning_st[8] = [0, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1200000, 1400000, 3000000]
#     binning_st[9] = [0, 500000, 700000, 800000, 900000, 1100000, 1400000, 3000000]
#     binning_st[10] = [0, 700000, 1000000, 1200000, 1500000, 3000000]

#     # rwt_ht = TTbarTrueFakePlot(rwt, "HT", "weight", (3000, 0, 3000000), array.array('d', binning_st[i]))
#     # drawStack(rwt_ht, "H_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_ht_fr_os" + suffix_before)

#     rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight", (3000, 0, 3000000), array.array('d', binning_st[i]))
#     drawStack(rwt_st, "S_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_st_fr_os" + suffix_before)

#     # rwt_njets = TTbarTrueFakePlot(rwt, "n_jets", "weight", (11, 2, 13))
#     # drawStack(rwt_njets, "# jets", regionTeX, f"plots/{i}jets/stack_njets_fr_os" + suffix_before)
    
#     print(f"{TermColor.OKBLUE}Yields (Before reweighting) {TermColor.ENDC}")
    
#     rwt_st.checkYields()

#     reweight1D(rwt_st, "S_{T} [MeV]", f"plots/{i}jets/wt1d_st_fr_os.pdf", f"_{i}jets")

#     # Apply reweighting
#     # ------------------

#     rwt.applyWeightNjets(("ST", os.path.join(os.getcwd(), "include", f"Reweight1D_{i}jets.h")), f"_{i}jets")

#     # After reweighting
#     # ------------------

#     rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight_new", (2000, 0, 2000000), array.array(
#         'd', [i for i in range(0, 2050000, 50000)]))
#     drawStack(rwt_st, "S_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_st_fr_os" + suffix_after)

#     rwt_njets = TTbarTrueFakePlot(rwt, "n_jets", "weight_new", (11, 2, 13))
#     drawStack(rwt_njets, "# jets", regionTeX, f"plots/{i}jets/stack_njets_fr_os" + suffix_after)

#     print(f"{TermColor.OKBLUE}Yields (After reweighting) {TermColor.ENDC}")

#     rwt_st.checkYields()

#     print(f"{TermColor.OKGREEN}Finished njets = {i}! {TermColor.ENDC}")

print(f"{TermColor.OKGREEN}All n jets are done! {TermColor.ENDC}")
del rwt

rwt = AnaTTbarTrueFake(tauid=False, isOS=True)

rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight", (2000, 0, 2000000))
print(f"{TermColor.OKBLUE}Yields (Before reweighting) {TermColor.ENDC}")
rwt_st.checkYields()

rwt.applyWeightStep1(("ST", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")), True)

rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight_new", (2000, 0, 2000000))
print(f"{TermColor.OKBLUE}Yields (After reweighting step 1) {TermColor.ENDC}")
rwt_st.checkYields()

# step 2 reweighting
# ------------------
print(f"{TermColor.OKBLUE}Second step reweighting with dRbb {TermColor.ENDC}")

binning_bb = [0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.6, 4, 4.5, 10]
rwt_dr_bb = TTbarTrueFakePlot(rwt, "dRbb", "weight_new", (100, 0, 10), rebin=array.array('d', binning_bb))
drawStack(rwt_dr_bb, "#DeltaR(b, b)", regionTeX, f"plots/dRbb/check_stack_dRbb_fr_os" + suffix_final)
reweight1D(rwt_dr_bb, "#DeltaR(b, b)", f"plots/dRbb/wt1d_dRbb_fr_os.pdf", f"_dRbb")

rwt.applyWeightStep2(("dRbb", os.path.join(os.getcwd(), "include", f"Reweight1D_dRbb.h")), True)
rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight_final", (2000, 0, 2000000))
print(f"{TermColor.OKBLUE}Yields (After reweighting step 2) {TermColor.ENDC}")
rwt_st.checkYields()

# step 3 reweighting
# ------------------
print(f"{TermColor.OKBLUE}Third step reweighting with dRTauLep {TermColor.ENDC}")

binning_lh = [0.2, 0.6, 1, 1.4, 1.8, 2.2, 2.6, 3, 3.4, 3.8, 4.2, 4.6, 5, 10]
rwt_dr_lh = TTbarTrueFakePlot(rwt, "dRTauLep", "weight_final", (100, 0, 10), rebin=array.array('d', binning_lh))
reweight1D(rwt_dr_lh, "#DeltaR(lep, #tau)", f"plots/dRlh/wt1d_dRlh_fr_os.pdf", f"_dRlh")

rwt.applyWeightStep3(("dRTauLep", os.path.join(os.getcwd(), "include", f"Reweight1D_dRlh.h")), True)
rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight_extra", (2000, 0, 2000000))
print(f"{TermColor.OKBLUE}Yields (After reweighting step 3) {TermColor.ENDC}")
rwt_st.checkYields()
