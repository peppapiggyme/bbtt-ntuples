import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

rwt = AnaTTbarTrueFake(tauid=False, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB > 150000. && mTW > 40000.", path=f"{os.getcwd()}/../fr-ntuple-v12/")

regionTeX = "lephad, OS, Mbb>150, MTW>40, Pass #tau ID"

suffix = f"_fakerate.pdf"

print(f"{TermColor.OKBLUE}Applying/or not applying tau SF and fake rate weight ... {TermColor.ENDC}")
rwt.applyTauSFAndFakeRate("Nominal") # only do tau SF weight

rwt_plot = TTbarTrueFakePlot(rwt, "MET", "Nominal_new", (400, 0, 400000), array.array(
    'd', [i for i in range(0, 420000, 20000)]))
drawStack(rwt_plot, "MET [MeV]", regionTeX, f"plots/fakerate/stack_met_fr_os" + suffix)
rwt_plot.checkYields()

rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "Nominal_new", (36, 20000, 200000))
drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/fakerate/stack_lep_ptlow_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "Nominal_new", (36, 20000, 200000))
drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/fakerate/stack_tau_ptlow_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "Nominal_new", (40, 50000, 250000))
drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/fakerate/stack_b0_ptlow_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "Nominal_new", (36, 20000, 200000))
drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/fakerate/stack_b1_ptlow_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "lep_pt", "Nominal_new", (380, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "lepton pT [MeV]", regionTeX, f"plots/fakerate/stack_lep_pt_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "tau_pt", "Nominal_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "tau pT [MeV]", regionTeX, f"plots/fakerate/stack_tau_pt_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "b0_pt", "Nominal_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "leading b-jet pT [MeV]", regionTeX, f"plots/fakerate/stack_b0_pt_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "b1_pt", "Nominal_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/fakerate/stack_b1_pt_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "mTW", "Nominal_new", (40, 40000, 240000))
drawStack(rwt_plot, "M_{T} [MeV]", regionTeX, f"plots/fakerate/stack_mtw_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "mBB", "Nominal_new", (40, 0, 400000))
drawStack(rwt_plot, "Mbb [MeV]", regionTeX, f"plots/fakerate/stack_mbb_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "mHH", "Nominal_new", (40, 200000, 2200000))
drawStack(rwt_plot, "Mhh [MeV]", regionTeX, f"plots/fakerate/stack_mhh_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "HT", "Nominal_new", (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot, "H_{T} [MeV]", regionTeX, f"plots/fakerate/stack_ht_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "ST", "Nominal_new", (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot, "S_{T} [MeV]", regionTeX, f"plots/fakerate/stack_st_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "n_jets", "Nominal_new", (11, 2, 13))
drawStack(rwt_plot, "# jets", regionTeX, f"plots/fakerate/stack_njets_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "lead_jet_pt", "Nominal_new", (50, 50000, 550000))
drawStack(rwt_plot, "leading jet pT [MeV]", regionTeX, f"plots/fakerate/stack_lead_jet_ptlow_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "dRTauLep", "Nominal_new", (36, 0, 6))
drawStack(rwt_plot, "#DeltaR(lep, #tau)", regionTeX, f"plots/fakerate/stack_dr_lep_tau_fr_os" + suffix)

rwt_plot = TTbarTrueFakePlot(rwt, "dRbb", "Nominal_new", (36, 0, 6))
drawStack(rwt_plot, "#DeltaR(b, b)", regionTeX, f"plots/fakerate/stack_dr_bb_fr_os" + suffix)


print(rwt_cn.numberOfSysts())
rwt_cn.checkYields()
