import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.EnableImplicitMT(2)

rwt = AnaTTbarIncl(tauid=False, isOS=True)

regionTeX = "lephad, OS, Mbb>150, MTW>50, No #tau ID"

df_njets = {}
for i in range(2, 11):
    df_njets[i] = {}

for p in rwt.processes:
    for i in range(2, 10):
        df_njets[i][p] = rwt.df[p].Filter("n_jets == " + str(i))
    df_njets[10][p] = rwt.df[p].Filter("n_jets >= 10")

for i in range(4, 11):
    print(f"{TermColor.BOLD}Analyzing number of jets = {i} (if i = 10, means #jets >= 10){TermColor.ENDC}")

    rwt.set_current_df(df_njets[i])

    # Before reweighting
    # ------------------

    suffix_before = f"_before.pdf"

    # rwt_lep_pt = TTbarInclPlot(rwt, "lep_pt", "weight", (380, 20000, 1000000), array.array(
    #     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    # drawStack(rwt_lep_pt, "lepton pT [MeV]", regionTeX, f"plots/{i}jets/stack_lep_pt_fr_os" + suffix_before)

    # rwt_met = TTbarInclPlot(rwt, "MET", "weight", (400, 0, 400000), array.array(
    #     'd', [i for i in range(0, 420000, 20000)]))
    # drawStack(rwt_met, "MET [MeV]", regionTeX, f"plots/{i}jets/stack_met_fr_os" + suffix_before)

    # rwt_metsig = TTbarInclPlot(rwt, "METSig", "weight", (20, 0, 20))
    # drawStack(rwt_metsig, "MET Significance", regionTeX, f"plots/{i}jets/stack_metsig_fr_os" + suffix_before)

    # rwt_tau_pt = TTbarInclPlot(rwt, "tau_pt", "weight", (980, 20000, 1000000), array.array(
    #     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    # drawStack(rwt_tau_pt, "tau pT [MeV]", regionTeX, f"plots/{i}jets/stack_tau_pt_fr_os" + suffix_before)

    # rwt_b0_pt = TTbarInclPlot(rwt, "b0_pt", "weight", (980, 20000, 1000000), array.array(
    #     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    # drawStack(rwt_b0_pt, "leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b0_pt_fr_os" + suffix_before)

    # rwt_b1_pt = TTbarInclPlot(rwt, "b1_pt", "weight", (980, 20000, 1000000), array.array(
    #     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    # drawStack(rwt_b1_pt, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b1_pt_fr_os" + suffix_before)

    # rwt_mtw = TTbarInclPlot(rwt, "mTW", "weight", (200, 50000, 250000), array.array(
    #     'd', [i for i in range(50000, 260000, 10000)]))
    # drawStack(rwt_mtw, "M_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_mtw_fr_os" + suffix_before)

    # rwt_mbb = TTbarInclPlot(rwt, "mBB", "weight", (500, 150000, 650000), array.array(
    #     'd', [i for i in range(150000, 670000, 20000)]))
    # drawStack(rwt_mbb, "Mbb [MeV]", regionTeX, f"plots/{i}jets/stack_mbb_fr_os" + suffix_before)

    # rwt_mhh = TTbarInclPlot(rwt, "mHH", "weight", (2000, 200000, 2200000), array.array(
    #     'd', [i for i in range(200000, 2200000, 50000)]))
    # drawStack(rwt_mhh, "Mhh [MeV]", regionTeX, f"plots/{i}jets/stack_mhh_fr_os" + suffix_before)

    rwt_ht = TTbarInclPlot(rwt, "HT", "weight", (2000, 0, 2000000), array.array(
        'd', [50000, 130000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 950000, 1000000, 1100000, 1200000, 1300000, 1400000, 1600000, 2000000]))
    drawStack(rwt_ht, "H_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_ht_fr_os" + suffix_before)

    rwt_st = TTbarInclPlot(rwt, "ST", "weight", (2000, 0, 2000000), array.array(
        'd', [50000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 1000000, 1200000, 2000000]))
    drawStack(rwt_st, "S_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_st_fr_os" + suffix_before)

    # rwt_stlephad = TTbarInclPlot(rwt, "STlephad", "weight", (1000, 0, 1000000), array.array(
    #     'd', [20000, 55000, 70000, 85000, 100000, 115000, 130000, 145000, 160000, 175000, 190000, 205000, 220000, 240000, 260000, 280000, 300000, 350000, 400000, 500000, 600000, 820000]))
    # drawStack(rwt_stlephad, "S_{T} (lep + tau) [MeV]", regionTeX, f"plots/{i}jets/stack_stlephad_fr_os" + suffix_before)

    # rwt_njets = TTbarInclPlot(rwt, "n_jets", "weight", (11, 0, 12))
    # drawStack(rwt_njets, "# jets", regionTeX, f"plots/{i}jets/stack_njets_fr_os" + suffix_before)

    rwt_st.checkYields()

    reweight1D(rwt_st, "S_{T} [MeV]", f"plots/{i}jets/wt1d_st_fr_os.pdf", f"_{i}jets")

    # Apply reweighting
    # ------------------

    rwt.applyWeightNjets(("ST", os.path.join(os.getcwd(), "include", f"Reweight1D_{i}jets.h")), f"_{i}jets")

    # After reweighting
    # ------------------

    suffix_after = f"_after.pdf"

    rwt_lep_pt = TTbarInclPlot(rwt, "lep_pt", "weight_new", (380, 20000, 1000000), array.array(
        'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    drawStack(rwt_lep_pt, "lepton pT [MeV]", regionTeX, f"plots/{i}jets/stack_lep_pt_fr_os" + suffix_after)

    rwt_met = TTbarInclPlot(rwt, "MET", "weight_new", (400, 0, 400000), array.array(
        'd', [i for i in range(0, 420000, 20000)]))
    drawStack(rwt_met, "MET [MeV]", regionTeX, f"plots/{i}jets/stack_met_fr_os" + suffix_after)

    rwt_metsig = TTbarInclPlot(rwt, "METSig", "weight_new", (20, 0, 20))
    drawStack(rwt_metsig, "MET Significance", regionTeX, f"plots/{i}jets/stack_metsig_fr_os" + suffix_after)

    rwt_tau_pt = TTbarInclPlot(rwt, "tau_pt", "weight_new", (980, 20000, 1000000), array.array(
        'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    drawStack(rwt_tau_pt, "tau pT [MeV]", regionTeX, f"plots/{i}jets/stack_tau_pt_fr_os" + suffix_after)

    rwt_b0_pt = TTbarInclPlot(rwt, "b0_pt", "weight_new", (980, 20000, 1000000), array.array(
        'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    drawStack(rwt_b0_pt, "leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b0_pt_fr_os" + suffix_after)

    rwt_b1_pt = TTbarInclPlot(rwt, "b1_pt", "weight_new", (980, 20000, 1000000), array.array(
        'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
    drawStack(rwt_b1_pt, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b1_pt_fr_os" + suffix_after)

    rwt_mtw = TTbarInclPlot(rwt, "mTW", "weight_new", (200, 50000, 250000), array.array(
        'd', [i for i in range(50000, 260000, 10000)]))
    drawStack(rwt_mtw, "M_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_mtw_fr_os" + suffix_after)

    rwt_mbb = TTbarInclPlot(rwt, "mBB", "weight_new", (500, 150000, 650000), array.array(
        'd', [i for i in range(150000, 670000, 20000)]))
    drawStack(rwt_mbb, "Mbb [MeV]", regionTeX, f"plots/{i}jets/stack_mbb_fr_os" + suffix_after)

    rwt_mhh = TTbarInclPlot(rwt, "mHH", "weight_new", (2000, 200000, 2200000), array.array(
        'd', [i for i in range(200000, 2200000, 50000)]))
    drawStack(rwt_mhh, "Mhh [MeV]", regionTeX, f"plots/{i}jets/stack_mhh_fr_os" + suffix_after)

    rwt_ht = TTbarInclPlot(rwt, "HT", "weight_new", (2000, 0, 2000000), array.array(
        'd', [i for i in range(0, 2050000, 50000)]))
    drawStack(rwt_ht, "H_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_ht_fr_os" + suffix_after)

    rwt_st = TTbarInclPlot(rwt, "ST", "weight_new", (2000, 0, 2000000), array.array(
        'd', [i for i in range(0, 2050000, 50000)]))
    drawStack(rwt_st, "S_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_st_fr_os" + suffix_after)

    rwt_stlephad = TTbarInclPlot(rwt, "STlephad", "weight_new", (1000, 20000, 820000), array.array(
        'd', [20000, 55000, 70000, 85000, 100000, 115000, 130000, 145000, 160000, 175000, 190000, 205000, 220000, 240000, 260000, 280000, 300000, 350000, 400000, 500000, 600000, 820000]))
    drawStack(rwt_stlephad, "S_{T} (lep + tau) [MeV]", regionTeX, f"plots/{i}jets/stack_stlephad_fr_os" + suffix_after)

    rwt_njets = TTbarInclPlot(rwt, "n_jets", "weight_new", (11, 0, 12))
    drawStack(rwt_njets, "# jets", regionTeX, f"plots/{i}jets/stack_njets_fr_os" + suffix_after)

    rwt_lep_pt.checkYields()
