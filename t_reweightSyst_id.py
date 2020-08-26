import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

#rwt = AnaTTbarTrueFake(tauid=True, isOS=True)
rwt = AnaTTbarTrueFake(tauid=True, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 150000.")

#regionTeX = "lephad, OS, Mbb sideband, MTW>60, Pass #tau ID"
regionTeX = "lephad, OS, Mbb sideband, MTW>150, Pass #tau ID"

suffix_syst = f"_tauid_syst.pdf"

variations = ["TTBarReweight_Stat1", "TTBarReweight_Stat2", "TTBarReweight_Stat3"]


print(f"{TermColor.OKBLUE}Applying/or not applying tau SF weight ... {TermColor.ENDC}")
rwt.applyTauSF("Nominal") # only do tau SF weight
for v in variations:
    rwt.applyTauSF(f"{v}__1up")
    rwt.applyTauSF(f"{v}__1down")

rwt_cn = TTbarSystPlotCollection(rwt, "mTW", "_new", variations, (40, 40000, 240000))
drawStack(rwt_cn.nominalPlot(), "M_{T} [MeV]", regionTeX, f"plots/after/stack_mtw_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "HT", "_new", variations, (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_cn.nominalPlot(), "H_{T} [MeV]", regionTeX, f"plots/after/stack_ht_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "ST", "_new", variations, (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_cn.nominalPlot(), "S_{T} [MeV]", regionTeX, f"plots/after/stack_st_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "lead_jet_pt", "_new", variations, (50, 50000, 550000))
drawStack(rwt_cn.nominalPlot(), "leading jet pT [MeV]", regionTeX, f"plots/after/stack_lead_jet_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "lep_pt", "_new", variations, (36, 20000, 200000))
drawStack(rwt_cn.nominalPlot(), "lepton pT [MeV]", regionTeX, f"plots/after/stack_lep_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "b0_pt", "_new", variations, (40, 50000, 250000))
drawStack(rwt_cn.nominalPlot(), "leading b-jet pT [MeV]", regionTeX, f"plots/after/stack_b0_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "b1_pt", "_new", variations, (36, 20000, 200000))
drawStack(rwt_cn.nominalPlot(), "sub-leading b-jet pT [MeV]", regionTeX, f"plots/after/stack_b1_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "tau_pt", "_new", variations, (36, 20000, 200000))
drawStack(rwt_cn.nominalPlot(), "tau pT [MeV]", regionTeX, f"plots/after/stack_tau_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "lep_pt", "_new", variations, (980, 20000, 1000000), array.array(
     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_cn.nominalPlot(), "lepton pT [MeV]", regionTeX, f"plots/after/stack_lep_pt_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "b0_pt", "_new", variations, (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_cn.nominalPlot(), "leading b-jet pT [MeV]", regionTeX, f"plots/after/stack_b0_pt_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "b1_pt", "_new", variations, (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_cn.nominalPlot(), "sub-leading b-jet pT [MeV]", regionTeX, f"plots/after/stack_b1_pt_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "tau_pt", "_new", variations, (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_cn.nominalPlot(), "tau pT [MeV]", regionTeX, f"plots/after/stack_tau_pt_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "n_jets", "_new", variations, (11, 2, 13))
drawStack(rwt_cn.nominalPlot(), "# jets", regionTeX, f"plots/after/stack_njets_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "MET", "_new", variations, (400, 0, 400000), array.array(
    'd', [i for i in range(0, 420000, 20000)]))
drawStack(rwt_cn.nominalPlot(), "MET [MeV]", regionTeX, f"plots/after/stack_met_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "mBB", "_new", variations, (40, 0, 400000))
drawStack(rwt_cn.nominalPlot(), "Mbb [MeV]", regionTeX, f"plots/after/stack_mbb_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "mHH", "_new", variations, (40, 200000, 2200000))
drawStack(rwt_cn.nominalPlot(), "Mhh [MeV]", regionTeX, f"plots/after/stack_mhh_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "dRbb", "_new", variations, (36, 0, 6))
drawStack(rwt_cn.nominalPlot(), "#DeltaR(b, b)", regionTeX, f"plots/after/stack_dr_bb_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "dRTauLep", "_new", variations, (36, 0, 6))
drawStack(rwt_cn.nominalPlot(), "#DeltaR(lep, #tau)", regionTeX, f"plots/after/stack_dr_lep_tau_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())


print(rwt_cn.numberOfSysts())
rwt_cn.checkYields()
