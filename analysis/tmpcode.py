# put tmp code here

# code for dRbb and dRll reweighting
# ==================================

# step 2 reweighting
# ------------------
print(f"{TermColor.OKBLUE}Second step reweighting with dRbb {TermColor.ENDC}")

binning_bb = [0.4, 0.8, 1.2, 1.6, 2, 2.2, 2.6, 2.8, 3.0, 3.2, 3.6, 4, 4.5, 10]
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

