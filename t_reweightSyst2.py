import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

# rwt = AnaTTbarTrueFake(tauid=False, isOS=True)
# norm = AnaTTbarTrueFake(tauid=False, isOS=True)

rwt = AnaTTbarTrueFake(tauid=False, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB < 150000. && mTW > 60000.")
norm = AnaTTbarTrueFake(tauid=False, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB < 150000. && mTW > 60000.")

#rwt = AnaTTbarTrueFake(tauid=True, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB > 150000. && mTW > 150000.")
#norm = AnaTTbarTrueFake(tauid=True, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB > 150000. && mTW > 150000.")

#regionTeX = "t#bar{t}-CR: Mbb>150, MTW>40, No #tau ID"
regionTeX = "RW-VR1: Mbb<150, MTW>60, No #tau ID"
#regionTeX = "RW-VR2: Mbb>150, MTW>150, Pass #tau ID"

#suffix_syst = f"_CR_syst.pdf"
suffix_syst = f"_VR1_syst.pdf"
#suffix_syst = f"_VR2_syst.pdf"

variations = ["TTBarReweight", "TTBarReweight_Stat", "TTBarReweight_Closure_TauPt"]

print(f"{TermColor.OKBLUE}Applying/or not applying tau SF weight ... {TermColor.ENDC}")
rwt.applyTauSF("RW_Nominal") # only do tau SF weight
for v in variations:
    rwt.applyTauSF(f"RW_{v}__1up")
    rwt.applyTauSF(f"RW_{v}__1down")

norm.applyTauSFAndTTBarNorm()

# rwt_cn = TTbarSystPlotCollection(rwt, "tau_eta", "RW_", "_new", variations, (40, -2.5, 2.5))
# drawStack(rwt_cn.nominalPlot(), "#tau #eta", regionTeX, f"plots/after/stack_tau_eta_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

# rwt_cn = TTbarSystPlotCollection(rwt, "dRbb", "RW_", "_new", variations, (36, 0, 6))
# drawStack(rwt_cn.nominalPlot(), "#DeltaR(b, b)", regionTeX, f"plots/after/stack_dr_bb_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

# rwt_cn = TTbarSystPlotCollection(rwt, "dRTauLep", "RW_", "_new", variations, (36, 0, 6))
# drawStack(rwt_cn.nominalPlot(), "#DeltaR(lep, #tau)", regionTeX, f"plots/after/stack_dr_lep_tau_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

# rwt_cn = TTbarSystPlotCollection(rwt, "lep_eta", "RW_", "_new", variations, (40, -2.5, 2.5))
# drawStack(rwt_cn.nominalPlot(), "lepton #eta", regionTeX, f"plots/after/stack_lep_eta_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

# rwt_cn = TTbarSystPlotCollection(rwt, "b0_eta", "RW_", "_new", variations, (40, -2.5, 2.5))
# drawStack(rwt_cn.nominalPlot(), "leading b-jet #eta", regionTeX, f"plots/after/stack_b0_eta_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

# rwt_cn = TTbarSystPlotCollection(rwt, "b1_eta", "RW_", "_new", variations, (40, -2.5, 2.5))
# drawStack(rwt_cn.nominalPlot(), "sub-leading b-jet #eta", regionTeX, f"plots/after/stack_b1_eta_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

# rwt_cn = TTbarSystPlotCollection(rwt, "tau_phi", "RW_", "_new", variations, (40, -3.14, 3.14))
# drawStack(rwt_cn.nominalPlot(), "#tau #phi", regionTeX, f"plots/after/stack_tau_phi_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

# rwt_cn = TTbarSystPlotCollection(rwt, "lep_phi", "RW_", "_new", variations, (40, -3.14, 3.14))
# drawStack(rwt_cn.nominalPlot(), "lepton #phi", regionTeX, f"plots/after/stack_lep_phi_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

# rwt_cn = TTbarSystPlotCollection(rwt, "b0_phi", "RW_", "_new", variations, (40, -3.14, 3.14))
# drawStack(rwt_cn.nominalPlot(), "leading b-jet #phi", regionTeX, f"plots/after/stack_b0_phi_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

# rwt_cn = TTbarSystPlotCollection(rwt, "b1_phi", "RW_", "_new", variations, (40, -3.14, 3.14))
# drawStack(rwt_cn.nominalPlot(), "sub-leading b-jet #phi", regionTeX, f"plots/after/stack_b1_phi_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

# rwt_cn = TTbarSystPlotCollection(rwt, "MET", "RW_", "_new", variations, (400, 0, 400000), array.array(
#     'd', [i for i in range(0, 420000, 20000)]))
# rwt_cn.checkYields()
# drawStack(rwt_cn.nominalPlot(), "MET [MeV]", regionTeX, f"plots/after/stack_met_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())
    
rwt_cn = TTbarSystPlotCollection(rwt, "mTW", "RW_", "_new", variations, (40, 40000, 240000))
norm_pt = TTbarTrueFakePlot(norm, "mTW", "weight_new", (40, 40000, 240000))
drawStack(rwt_cn.nominalPlot(), "m_{T}^{W} [MeV]", regionTeX, f"plots/after/stack_mtw_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

# rwt_cn = TTbarSystPlotCollection(rwt, "HT", "RW_", "_new", variations, (2000, 0, 2000000), array.array(
#     'd', [i for i in range(0, 2050000, 50000)]))
# drawStack(rwt_cn.nominalPlot(), "H_{T} [MeV]", regionTeX, f"plots/after/stack_ht_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "ST", "RW_", "_new", variations, (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
norm_pt = TTbarTrueFakePlot(norm, "ST", "weight_new", (2000, 0, 2000000), array.array(
    'd', [i for i in range(0, 2050000, 50000)]))
drawStack(rwt_cn.nominalPlot(), "H_{T} [MeV]", regionTeX, f"plots/after/stack_st_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

# rwt_cn = TTbarSystPlotCollection(rwt, "lead_jet_pt", "RW_", "_new", variations, (50, 50000, 550000))
# drawStack(rwt_cn.nominalPlot(), "leading jet pT [MeV]", regionTeX, f"plots/after/stack_lead_jet_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots())

rwt_cn = TTbarSystPlotCollection(rwt, "lep_pt", "RW_", "_new", variations, (36, 20000, 200000))
norm_pt = TTbarTrueFakePlot(norm, "lep_pt", "weight_new", (36, 20000, 200000))
drawStack(rwt_cn.nominalPlot(), "e/#mu p_{T} [MeV]", regionTeX, f"plots/after/stack_lep_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

rwt_cn = TTbarSystPlotCollection(rwt, "b0_pt", "RW_", "_new", variations, (40, 50000, 250000))
norm_pt = TTbarTrueFakePlot(norm, "b0_pt", "weight_new", (40, 50000, 250000))
drawStack(rwt_cn.nominalPlot(), "leading b-jet p_{T} [MeV]", regionTeX, f"plots/after/stack_b0_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

rwt_cn = TTbarSystPlotCollection(rwt, "b1_pt", "RW_", "_new", variations, (36, 20000, 200000))
norm_pt = TTbarTrueFakePlot(norm, "b1_pt", "weight_new", (36, 20000, 200000))
drawStack(rwt_cn.nominalPlot(), "sub-leading b-jet p_{T} [MeV]", regionTeX, f"plots/after/stack_b1_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

rwt_cn = TTbarSystPlotCollection(rwt, "tau_pt", "RW_", "_new", variations, (36, 20000, 200000))
norm_pt = TTbarTrueFakePlot(norm, "tau_pt", "weight_new", (36, 20000, 200000))
drawStack(rwt_cn.nominalPlot(), "#tau_{had} p_{T} [MeV]", regionTeX, f"plots/after/stack_tau_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

rwt_cn = TTbarSystPlotCollection(rwt, "lep_pt", "RW_", "_new", variations, (980, 20000, 1000000), array.array(
     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 400000, 1000000]))
norm_pt = TTbarTrueFakePlot(norm, "lep_pt", "weight_new", (980, 20000, 1000000), array.array(
     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 400000, 1000000]))
drawStack(rwt_cn.nominalPlot(), "e/#mu p_{T} [MeV]", regionTeX, f"plots/after/stack_lep_pt_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

rwt_cn = TTbarSystPlotCollection(rwt, "b0_pt", "RW_", "_new", variations, (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 400000, 1000000]))
norm_pt = TTbarTrueFakePlot(norm, "b0_pt", "weight_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 400000, 1000000]))
drawStack(rwt_cn.nominalPlot(), "leading b-jet p_{T} [MeV]", regionTeX, f"plots/after/stack_b0_pt_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

rwt_cn = TTbarSystPlotCollection(rwt, "b1_pt", "RW_", "_new", variations, (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
norm_pt = TTbarTrueFakePlot(norm, "b1_pt", "weight_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_cn.nominalPlot(), "sub-leading b-jet p_{T} [MeV]", regionTeX, f"plots/after/stack_b1_pt_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

rwt_cn = TTbarSystPlotCollection(rwt, "tau_pt", "RW_", "_new", variations, (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
norm_pt = TTbarTrueFakePlot(norm, "tau_pt", "weight_new", (980, 20000, 1000000), array.array(
    'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
drawStack(rwt_cn.nominalPlot(), "#tau_{had} p_{T} [MeV]", regionTeX, f"plots/after/stack_tau_pt_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

rwt_cn = TTbarSystPlotCollection(rwt, "n_jets", "RW_", "_new", variations, (11, 2, 13))
norm_pt = TTbarTrueFakePlot(norm, "n_jets", "weight_new", (11, 2, 13))
drawStack(rwt_cn.nominalPlot(), "N_{jets}", regionTeX, f"plots/after/stack_njets_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

rwt_cn = TTbarSystPlotCollection(rwt, "mBB", "RW_", "_new", variations, (40, 0, 400000))
norm_pt = TTbarTrueFakePlot(norm, "mBB", "weight_new", (40, 0, 400000))
drawStack(rwt_cn.nominalPlot(), "m_{bb} [MeV]", regionTeX, f"plots/after/stack_mbb_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

rwt_cn = TTbarSystPlotCollection(rwt, "mHH", "RW_", "_new", variations, (40, 200000, 2200000))
norm_pt = TTbarTrueFakePlot(norm, "mHH", "weight_new", (40, 200000, 2200000))
drawStack(rwt_cn.nominalPlot(), "m_{hh} [MeV]", regionTeX, f"plots/after/stack_mhh_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_pt)

print(rwt_cn.numberOfSysts())
rwt_cn.checkYields()
