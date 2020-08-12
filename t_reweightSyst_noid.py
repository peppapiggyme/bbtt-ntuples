import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

rwt = AnaTTbarTrueFake(tauid=False, isOS=True, path=f"{os.getcwd()}/../fr-ntuple-v7/")
#rwt = AnaTTbarTrueFake(tauid=False, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB < 150000. && mTW > 40000.", path=f"{os.getcwd()}/../fr-ntuple-v7/")

regionTeX = "lephad, OS, Mbb sideband (50~100, 150~350), MTW>40, No #tau ID"
#regionTeX = "lephad, OS, Mbb window (100~150), MTW>40, No #tau ID"

suffix_syst = f"_syst.pdf"

variations = ["TTBarReweight_Stat", "TTBarReweight_Closure_TauPt", "TTBarReweight_Closure_dRbb"]
# variations = ["TTBarReweight_Stat", "TTBarReweight_Closure2"]

print(f"{TermColor.OKBLUE}Applying/or not applying tau SF weight ... {TermColor.ENDC}")
rwt.applyTauSF("Nominal") # only do tau SF weight
for v in variations:
    rwt.applyTauSF(f"{v}__1up")
    rwt.applyTauSF(f"{v}__1down")

rwt_plot = TTbarSystPlotCollection(rwt, "mTW", "_new", variations, (40, 40000, 240000))
drawStack(rwt_plot.nominalPlot(), "M_{T} [MeV]", regionTeX, f"plots/after/stack_mtw_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "HT", "_new", variations, (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot.nominalPlot(), "H_{T} [MeV]", regionTeX, f"plots/after/stack_ht_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "ST", "_new", variations, (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_plot.nominalPlot(), "S_{T} [MeV]", regionTeX, f"plots/after/stack_st_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "lead_jet_pt", "_new", variations, (50, 50000, 550000))
drawStack(rwt_plot.nominalPlot(), "leading jet pT [MeV]", regionTeX, f"plots/after/stack_lead_jet_ptlow_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "lep_pt", "_new", variations, (36, 20000, 200000))
drawStack(rwt_plot.nominalPlot(), "lepton pT [MeV]", regionTeX, f"plots/after/stack_lep_ptlow_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "b0_pt", "_new", variations, (40, 50000, 250000))
drawStack(rwt_plot.nominalPlot(), "leading b-jet pT [MeV]", regionTeX, f"plots/after/stack_b0_ptlow_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "b1_pt", "_new", variations, (36, 20000, 200000))
drawStack(rwt_plot.nominalPlot(), "sub-leading b-jet pT [MeV]", regionTeX, f"plots/after/stack_b1_ptlow_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "tau_pt", "_new", variations, (36, 20000, 200000))
drawStack(rwt_plot.nominalPlot(), "tau pT [MeV]", regionTeX, f"plots/after/stack_tau_ptlow_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "lep_pt", "_new", variations, (980, 20000, 1000000), array.array(
     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot.nominalPlot(), "lepton pT [MeV]", regionTeX, f"plots/after/stack_lep_pt_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "b0_pt", "_new", variations, (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot.nominalPlot(), "leading b-jet pT [MeV]", regionTeX, f"plots/after/stack_b0_pt_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "b1_pt", "_new", variations, (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot.nominalPlot(), "sub-leading b-jet pT [MeV]", regionTeX, f"plots/after/stack_b1_pt_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "tau_pt", "_new", variations, (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_plot.nominalPlot(), "tau pT [MeV]", regionTeX, f"plots/after/stack_tau_pt_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "n_jets", "_new", variations, (11, 2, 13))
drawStack(rwt_plot.nominalPlot(), "# jets", regionTeX, f"plots/after/stack_njets_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "MET", "_new", variations, (400, 0, 400000), array.array(
    'd', [i for i in range(0, 420000, 20000)]))
drawStack(rwt_plot.nominalPlot(), "MET [MeV]", regionTeX, f"plots/after/stack_met_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "mBB", "_new", variations, (40, 0, 400000), array.array(
    'd', [i for i in range(0, 155000, 5000)]))
drawStack(rwt_plot.nominalPlot(), "Mbb [MeV]", regionTeX, f"plots/after/stack_mbb_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "mHH", "_new", variations, (40, 200000, 2200000))
drawStack(rwt_plot.nominalPlot(), "Mhh [MeV]", regionTeX, f"plots/after/stack_mhh_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "dRbb", "_new", variations, (36, 0, 6))
drawStack(rwt_plot.nominalPlot(), "#DeltaR(b, b)", regionTeX, f"plots/after/stack_dr_bb_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())

rwt_plot = TTbarSystPlotCollection(rwt, "dRTauLep", "_new", variations, (36, 0, 6))
drawStack(rwt_plot.nominalPlot(), "#DeltaR(lep, #tau)", regionTeX, f"plots/after/stack_dr_lep_tau_fr_os" + suffix_syst, systs=rwt_plot.systematicPlots())


print(rwt_plot.numberOfSysts())
rwt_plot.checkYields()
