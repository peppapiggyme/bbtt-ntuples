import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.EnableImplicitMT(2)

rwt = AnaTTbarIncl(tauid=False, isOS=True)

# Before reweighting
# ------------------

rwt_lep_pt = TTbarInclPlot(rwt, "lep_pt", "weight", (380, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_lep_pt, "lepton pT [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_lep_pt_fr_os_before.pdf")

rwt_met = TTbarInclPlot(rwt, "MET", "weight", (400, 0, 400000), array.array(
    'd', [i for i in range(0, 420000, 20000)]))
drawStack(rwt_met, "MET [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_met_fr_os_before.pdf")

rwt_metsig = TTbarInclPlot(rwt, "METSig", "weight", (20, 0, 20))
drawStack(rwt_metsig, "MET Significance",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_metsig_fr_os_before.pdf")

rwt_tau_pt = TTbarInclPlot(rwt, "tau_pt", "weight", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_tau_pt, "tau pT [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_tau_pt_fr_os_before.pdf")

rwt_b0_pt = TTbarInclPlot(rwt, "b0_pt", "weight", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_b0_pt, "leading b-jet pT [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_b0_pt_fr_os_before.pdf")

rwt_b1_pt = TTbarInclPlot(rwt, "b1_pt", "weight", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_b1_pt, "sub-leading b-jet pT [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_b1_pt_fr_os_before.pdf")

rwt_mtw = TTbarInclPlot(rwt, "mTW", "weight", (200, 0, 200000), array.array(
    'd', [i for i in range(0, 210000, 10000)]))
drawStack(rwt_mtw, "M_{T} [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_mtw_fr_os_before.pdf")

rwt_mbb = TTbarInclPlot(rwt, "mBB", "weight", (500, 150000, 650000), array.array(
    'd', [i for i in range(150000, 670000, 20000)]))
drawStack(rwt_mbb, "Mbb [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_mbb_fr_os_before.pdf")

rwt_mhh = TTbarInclPlot(rwt, "mHH", "weight", (3000, 0, 3000000), array.array(
    'd', [i for i in range(0, 3050000, 50000)]))
drawStack(rwt_mhh, "Mhh [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_mhh_fr_os_before.pdf")

rwt_ht = TTbarInclPlot(rwt, "HT", "weight", (3000, 0, 3000000), array.array(
    'd', [i for i in range(0, 3050000, 50000)]))
drawStack(rwt_ht, "H_{T} [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_ht_fr_os_before.pdf")

rwt_st = TTbarInclPlot(rwt, "ST", "weight", (3000, 0, 3000000), array.array(
    'd', [i for i in range(0, 3050000, 50000)]))
drawStack(rwt_st, "S_{T} [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_st_fr_os_before.pdf")

rwt_stlephad = TTbarInclPlot(rwt, "STlephad", "weight", (3000, 0, 3000000), array.array(
    'd', [i for i in range(0, 3050000, 50000)]))
drawStack(rwt_stlephad, "S_{T} (lep + tau) [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_stlephad_fr_os_before.pdf")

rwt_njets = TTbarInclPlot(rwt, "n_jets", "weight", (10, 0, 11))
drawStack(rwt_njets, "# jets",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_njets_fr_os_before.pdf")


rwt_lep_pt.checkYields()

reweight1D(rwt_tau_pt, "tau pT [MeV]", "plots/wt1d_tau_pt_fr_os.pdf")

# Apply reweighting
# ------------------

rwt.applyWeight(("tau_pt", os.path.join(
    os.getcwd(), "include", "Reweight1D.h")))

# After reweighting
# ------------------

rwt_lep_pt = TTbarInclPlot(rwt, "lep_pt", "weight_new", (380, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_lep_pt, "lepton pT [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_lep_pt_fr_os_after.pdf")

rwt_met = TTbarInclPlot(rwt, "MET", "weight_new", (400, 0, 400000), array.array(
    'd', [i for i in range(0, 420000, 20000)]))
drawStack(rwt_met, "MET [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_met_fr_os_after.pdf")

rwt_metsig = TTbarInclPlot(rwt, "METSig", "weight_new", (20, 0, 20))
drawStack(rwt_metsig, "MET Significance",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_metsig_fr_os_after.pdf")

rwt_tau_pt = TTbarInclPlot(rwt, "tau_pt", "weight_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_tau_pt, "tau pT [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_tau_pt_fr_os_after.pdf")

rwt_b0_pt = TTbarInclPlot(rwt, "b0_pt", "weight_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_b0_pt, "leading b-jet pT [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_b0_pt_fr_os_after.pdf")

rwt_b1_pt = TTbarInclPlot(rwt, "b1_pt", "weight_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_b1_pt, "sub-leading b-jet pT [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_b1_pt_fr_os_after.pdf")

rwt_mtw = TTbarInclPlot(rwt, "mTW", "weight_new", (200, 0, 200000), array.array(
    'd', [i for i in range(0, 210000, 10000)]))
drawStack(rwt_mtw, "M_{T} [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_mtw_fr_os_after.pdf")

rwt_mbb = TTbarInclPlot(rwt, "mBB", "weight_new", (500, 150000, 650000), array.array(
    'd', [i for i in range(150000, 670000, 20000)]))
drawStack(rwt_mbb, "Mbb [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_mbb_fr_os_after.pdf")

rwt_mhh = TTbarInclPlot(rwt, "mHH", "weight_new", (3000, 0, 3000000), array.array(
    'd', [i for i in range(0, 3050000, 50000)]))
drawStack(rwt_mhh, "Mhh [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_mhh_fr_os_after.pdf")

rwt_ht = TTbarInclPlot(rwt, "HT", "weight_new", (3000, 0, 3000000), array.array(
    'd', [i for i in range(0, 3050000, 50000)]))
drawStack(rwt_ht, "H_{T} [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_ht_fr_os_after.pdf")

rwt_st = TTbarInclPlot(rwt, "ST", "weight_new", (3000, 0, 3000000), array.array(
    'd', [i for i in range(0, 3050000, 50000)]))
drawStack(rwt_st, "S_{T} [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_st_fr_os_after.pdf")

rwt_stlephad = TTbarInclPlot(rwt, "STlephad", "weight_new", (3000, 0, 3000000), array.array(
    'd', [i for i in range(0, 3050000, 50000)]))
drawStack(rwt_stlephad, "S_{T} (lep + tau) [MeV]",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_stlephad_fr_os_after.pdf")

rwt_njets = TTbarInclPlot(rwt, "n_jets", "weight_new", (10, 0, 11))
drawStack(rwt_njets, "# jets",
          "lephad, OS, Mbb>150, MTW>50, No #tau ID", "plots/stack_njets_fr_os_after.pdf")

rwt_lep_pt.checkYields()
