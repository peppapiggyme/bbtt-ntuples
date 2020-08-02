import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

print(f"{TermColor.OKBLUE}Starting program ... {TermColor.ENDC}")

R.EnableImplicitMT(2)

rwt = AnaTTbarTrueFale(tauid=False, isOS=True)

regionTeX = "lephad, OS, Mbb>150, MTW>40, No #tau ID"

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

    # rwt_lep_pt = TTbarTrueFakePlot(rwt, "lep_pt", "weight", (380, 20000, 1000000), array.array(
    #     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    # drawStack(rwt_lep_pt, "lepton pT [MeV]", regionTeX, f"plots/{i}jets/stack_lep_pt_fr_os" + suffix_before)

    # rwt_met = TTbarTrueFakePlot(rwt, "MET", "weight", (400, 0, 400000), array.array(
    #     'd', [i for i in range(0, 420000, 20000)]))
    # drawStack(rwt_met, "MET [MeV]", regionTeX, f"plots/{i}jets/stack_met_fr_os" + suffix_before)

    # rwt_metsig = TTbarTrueFakePlot(rwt, "METSig", "weight", (20, 0, 20))
    # drawStack(rwt_metsig, "MET Significance", regionTeX, f"plots/{i}jets/stack_metsig_fr_os" + suffix_before)

    # rwt_tau_pt = TTbarTrueFakePlot(rwt, "tau_pt", "weight", (980, 20000, 1000000), array.array(
    #     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    # drawStack(rwt_tau_pt, "tau pT [MeV]", regionTeX, f"plots/{i}jets/stack_tau_pt_fr_os" + suffix_before)

    # rwt_b0_pt = TTbarTrueFakePlot(rwt, "b0_pt", "weight", (980, 20000, 1000000), array.array(
    #     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    # drawStack(rwt_b0_pt, "leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b0_pt_fr_os" + suffix_before)

    # rwt_b1_pt = TTbarTrueFakePlot(rwt, "b1_pt", "weight", (980, 20000, 1000000), array.array(
    #     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    # drawStack(rwt_b1_pt, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b1_pt_fr_os" + suffix_before)

    # rwt_mtw = TTbarTrueFakePlot(rwt, "mTW", "weight", (200, 40000, 240000), array.array(
    #     'd', [i for i in range(50000, 260000, 10000)]))
    # drawStack(rwt_mtw, "M_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_mtw_fr_os" + suffix_before)

    # rwt_mbb = TTbarTrueFakePlot(rwt, "mBB", "weight", (500, 150000, 650000), array.array(
    #     'd', [i for i in range(150000, 670000, 20000)]))
    # drawStack(rwt_mbb, "Mbb [MeV]", regionTeX, f"plots/{i}jets/stack_mbb_fr_os" + suffix_before)

    # rwt_mhh = TTbarTrueFakePlot(rwt, "mHH", "weight", (2000, 200000, 2200000), array.array(
    #     'd', [i for i in range(200000, 2200000, 50000)]))
    # drawStack(rwt_mhh, "Mhh [MeV]", regionTeX, f"plots/{i}jets/stack_mhh_fr_os" + suffix_before)

    binning_st = None
    if i <= 5:
        binning_st = [50000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 1000000, 1200000, 3000000]
    elif i > 5 and i <= 7:
        binning_st = [50000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 1000000, 1200000, 2000000, 3000000]
    else:
        binning_st = [50000, 400000, 600000, 800000, 1000000, 1200000, 1400000, 1800000, 2200000, 2600000, 3000000]

    rwt_ht = TTbarTrueFakePlot(rwt, "HT", "weight", (3000, 0, 3000000), array.array('d', binning_st))
    drawStack(rwt_ht, "H_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_ht_fr_os" + suffix_before)

    # rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight", (3000, 0, 3000000), array.array('d', binning_st))
    # drawStack(rwt_st, "S_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_st_fr_os" + suffix_before)

    # rwt_stlephad = TTbarTrueFakePlot(rwt, "STlephad", "weight", (1000, 0, 1000000), array.array(
    #     'd', [20000, 55000, 70000, 85000, 100000, 115000, 130000, 145000, 160000, 175000, 190000, 205000, 220000, 240000, 260000, 280000, 300000, 350000, 400000, 500000, 600000, 820000]))
    # drawStack(rwt_stlephad, "S_{T} (lep + tau) [MeV]", regionTeX, f"plots/{i}jets/stack_stlephad_fr_os" + suffix_before)

    # rwt_njets = TTbarTrueFakePlot(rwt, "n_jets", "weight", (11, 2, 13))
    # drawStack(rwt_njets, "# jets", regionTeX, f"plots/{i}jets/stack_njets_fr_os" + suffix_before)
    
    print(f"{TermColor.OKBLUE}Yields (Before reweighting) {TermColor.ENDC}")
    
    rwt_ht.checkYields()

    reweight1D(rwt_ht, "H_{T} [MeV]", f"plots/{i}jets/wt1d_ht_fr_os.pdf", f"_{i}jets")

    # Apply reweighting
    # ------------------

    rwt.applyWeightNjets(("ST", os.path.join(os.getcwd(), "include", f"Reweight1D_{i}jets.h")), f"_{i}jets")

    # After reweighting
    # ------------------

    suffix_after = f"_after.pdf"

    rwt_lep_pt = TTbarTrueFakePlot(rwt, "lep_pt", "weight_new", (380, 20000, 1000000), array.array(
        'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    drawStack(rwt_lep_pt, "lepton pT [MeV]", regionTeX, f"plots/{i}jets/stack_lep_pt_fr_os" + suffix_after)

    rwt_met = TTbarTrueFakePlot(rwt, "MET", "weight_new", (400, 0, 400000), array.array(
        'd', [i for i in range(0, 420000, 20000)]))
    drawStack(rwt_met, "MET [MeV]", regionTeX, f"plots/{i}jets/stack_met_fr_os" + suffix_after)

    rwt_metsig = TTbarTrueFakePlot(rwt, "METSig", "weight_new", (20, 0, 20))
    drawStack(rwt_metsig, "MET Significance", regionTeX, f"plots/{i}jets/stack_metsig_fr_os" + suffix_after)

    rwt_tau_pt = TTbarTrueFakePlot(rwt, "tau_pt", "weight_new", (980, 20000, 1000000), array.array(
        'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    drawStack(rwt_tau_pt, "tau pT [MeV]", regionTeX, f"plots/{i}jets/stack_tau_pt_fr_os" + suffix_after)

    rwt_b0_pt = TTbarTrueFakePlot(rwt, "b0_pt", "weight_new", (980, 20000, 1000000), array.array(
        'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    drawStack(rwt_b0_pt, "leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b0_pt_fr_os" + suffix_after)

    rwt_b1_pt = TTbarTrueFakePlot(rwt, "b1_pt", "weight_new", (980, 20000, 1000000), array.array(
        'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    drawStack(rwt_b1_pt, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b1_pt_fr_os" + suffix_after)

    rwt_mtw = TTbarTrueFakePlot(rwt, "mTW", "weight_new", (200, 40000, 240000), array.array(
        'd', [i for i in range(50000, 260000, 10000)]))
    drawStack(rwt_mtw, "M_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_mtw_fr_os" + suffix_after)

    rwt_mbb = TTbarTrueFakePlot(rwt, "mBB", "weight_new", (500, 150000, 650000), array.array(
        'd', [i for i in range(150000, 670000, 20000)]))
    drawStack(rwt_mbb, "Mbb [MeV]", regionTeX, f"plots/{i}jets/stack_mbb_fr_os" + suffix_after)

    rwt_mhh = TTbarTrueFakePlot(rwt, "mHH", "weight_new", (2000, 200000, 2200000), array.array(
        'd', [i for i in range(200000, 2200000, 50000)]))
    drawStack(rwt_mhh, "Mhh [MeV]", regionTeX, f"plots/{i}jets/stack_mhh_fr_os" + suffix_after)

    rwt_ht = TTbarTrueFakePlot(rwt, "HT", "weight_new", (2000, 0, 2000000), array.array(
        'd', [i for i in range(0, 2050000, 50000)]))
    drawStack(rwt_ht, "H_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_ht_fr_os" + suffix_after)

    rwt_st = TTbarTrueFakePlot(rwt, "ST", "weight_new", (2000, 0, 2000000), array.array(
        'd', [i for i in range(0, 2050000, 50000)]))
    drawStack(rwt_st, "S_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_st_fr_os" + suffix_after)

    rwt_stlephad = TTbarTrueFakePlot(rwt, "STlephad", "weight_new", (1000, 20000, 820000), array.array(
        'd', [20000, 55000, 70000, 85000, 100000, 115000, 130000, 145000, 160000, 175000, 190000, 205000, 220000, 240000, 260000, 280000, 300000, 350000, 400000, 500000, 600000, 820000]))
    drawStack(rwt_stlephad, "S_{T} (lep + tau) [MeV]", regionTeX, f"plots/{i}jets/stack_stlephad_fr_os" + suffix_after)

    rwt_njets = TTbarTrueFakePlot(rwt, "n_jets", "weight_new", (11, 2, 13))
    drawStack(rwt_njets, "# jets", regionTeX, f"plots/{i}jets/stack_njets_fr_os" + suffix_after)

    print(f"{TermColor.OKBLUE}Yields (After reweighting) {TermColor.ENDC}")

    rwt_lep_pt.checkYields()

    print(f"{TermColor.OKGREEN}Finished njets = {i}! {TermColor.ENDC}")

print(f"{TermColor.OKGREEN}All n jets are done! {TermColor.ENDC}")
