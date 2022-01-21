import ROOT as R
import os, sys
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

region = sys.argv[1]

# rwt = AnaTTbarTrueFake(tauid=True, isOS=True, rewrite="n_btag == 2 && n_jets > 2 && mBB < 150000.")
# norm = AnaTTbarTrueFake(tauid=True, isOS=True, rewrite="n_btag == 2 && n_jets > 2 && mBB < 150000.")
# regionTeX = "LepHad SLT SR"
# suffix_syst = f"_SLT_SR_syst.pdf"

rwt = None
norm = None
regionTeX = None
suffix_syst = None

if region == "0":
    rwt = AnaTTbarTrueFake(tauid=False, isOS=True)
    norm = AnaTTbarTrueFake(tauid=False, isOS=True)
    regionTeX = "t#bar{t}-noID-CR"
    suffix_syst = f"_CR_syst.pdf"

elif region == "1":
    rwt = AnaTTbarTrueFake(tauid=False, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && ((mBB > 50000 && mBB < 800000.) || (mBB > 140000. && mBB < 150000.)) && mTW > 40000.")
    norm = AnaTTbarTrueFake(tauid=False, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && ((mBB > 50000 && mBB < 800000.) || (mBB > 140000. && mBB < 150000.)) && mTW > 40000.")
    regionTeX = "t#bar{t}-VR1 (noID, low m_{bb})"
    suffix_syst = f"_VR1_syst.pdf"

elif region == "2":
    rwt = AnaTTbarTrueFake(tauid=True, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB > 150000. && mTW > 140000.")
    norm = AnaTTbarTrueFake(tauid=True, isOS=True, rewrite="n_btag == 2 && n_jets >= 2 && mBB > 150000. && mTW > 140000.")
    regionTeX = "t#bar{t}-VR2 (LooseID, high m_{T}^{W})"
    suffix_syst = f"_VR2_syst.pdf"

ratrng = (0.78, 1.22)

variations = ["TTBarReweight", "TTBarReweight_Stat", "TTBarReweight_Closure_TauPt"]

print(f"{TermColor.OKBLUE}Applying/or not applying tau SF weight ... {TermColor.ENDC}")

norm_factor = TTbarTrueFakePlot(rwt, "n_jets", "weight", (11, 2, 13)).checkTTBarNorm()
norm_factor_nominal = TTbarTrueFakePlot(rwt, "n_jets", "RW_Nominal", (11, 2, 13)).checkTTBarNorm()
rwt.applyTauSFAndTTBarNorm("RW_Nominal", "RW_normalised_Nominal_new", norm_factor=norm_factor_nominal) # only do tau SF weight

for v in variations:
    rwt.applyTauSFAndTTBarNorm(f"RW_{v}__1up", f"RW_normalised_{v}__1up_new", norm_factor=norm_factor_nominal)
    rwt.applyTauSFAndTTBarNorm(f"RW_{v}__1down", f"RW_normalised_{v}__1down_new", norm_factor=norm_factor_nominal)

norm.applyTauSFAndTTBarNorm(norm_factor=norm_factor)

rwt.add_var("ST_GeV", "ST / 1e3")
norm.add_var("ST_GeV", "ST / 1e3")

rwt.add_var("lep_pt_GeV", "lep_pt / 1e3")
norm.add_var("lep_pt_GeV", "lep_pt / 1e3")

rwt.add_var("tau_pt_GeV", "tau_pt / 1e3")
norm.add_var("tau_pt_GeV", "tau_pt / 1e3")

rwt.add_var("b0_pt_GeV", "b0_pt / 1e3")
norm.add_var("b0_pt_GeV", "b0_pt / 1e3")

rwt.add_var("b1_pt_GeV", "b1_pt / 1e3")
norm.add_var("b1_pt_GeV", "b1_pt / 1e3")

rwt.add_var("mTW_GeV", "mTW / 1e3")
norm.add_var("mTW_GeV", "mTW / 1e3")

rwt_cn = TTbarSystPlotCollection(rwt, "n_jets", "RW_normalised_", "_new", variations, (11, 2, 13))
norm_plt = TTbarTrueFakePlot(norm, "n_jets", "weight_new", (11, 2, 13))
drawStack(rwt_cn.nominalPlot(), "N_{jets}", regionTeX, f"forThesis/after/stack_njets_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_plt, ratio_range=ratrng)

rwt_cn = TTbarSystPlotCollection(rwt, "ST_GeV", "RW_normalised_", "_new", variations, (1500, 0, 1500), array.array('d', [i for i in range(0, 1530, 30)]))
norm_plt = TTbarTrueFakePlot(norm, "ST_GeV", "weight_new", (1500, 0, 1500), array.array('d', [i for i in range(0, 1530, 30)]))
drawStack(rwt_cn.nominalPlot(), "H_{T} [GeV]", regionTeX, f"forThesis/after/stack_st_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_plt, ratio_range=ratrng)

rwt_cn = TTbarSystPlotCollection(rwt, "lep_pt_GeV", "RW_normalised_", "_new", variations, (50, 0, 250))
norm_plt = TTbarTrueFakePlot(norm, "lep_pt_GeV", "weight_new", (50, 0, 250))
drawStack(rwt_cn.nominalPlot(), "e/#mu p_{T} [GeV]", regionTeX, f"forThesis/after/stack_lep_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_plt, ratio_range=ratrng)

rwt_cn = TTbarSystPlotCollection(rwt, "tau_pt_GeV", "RW_normalised_", "_new", variations, (50, 0, 250))
norm_plt = TTbarTrueFakePlot(norm, "tau_pt_GeV", "weight_new", (50, 0, 250))
drawStack(rwt_cn.nominalPlot(), "#tau_{had} p_{T} [GeV]", regionTeX, f"forThesis/after/stack_tau_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_plt, ratio_range=ratrng)

rwt_cn = TTbarSystPlotCollection(rwt, "b0_pt_GeV", "RW_normalised_", "_new", variations, (50, 0, 250))
norm_plt = TTbarTrueFakePlot(norm, "b0_pt_GeV", "weight_new", (50, 0, 250))
drawStack(rwt_cn.nominalPlot(), "Leading b-jet p_{T} [GeV]", regionTeX, f"forThesis/after/stack_b0_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_plt, ratio_range=ratrng)

rwt_cn = TTbarSystPlotCollection(rwt, "b1_pt_GeV", "RW_normalised_", "_new", variations, (50, 0, 250))
norm_plt = TTbarTrueFakePlot(norm, "b1_pt_GeV", "weight_new", (50, 0, 250))
drawStack(rwt_cn.nominalPlot(), "Sub-leading b-jet p_{T} [GeV]", regionTeX, f"forThesis/after/stack_b1_ptlow_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_plt, ratio_range=ratrng)

rwt_cn = TTbarSystPlotCollection(rwt, "mTW_GeV", "RW_normalised_", "_new", variations, (50, 40, 240) if region != "2" else (50, 140, 340))
norm_plt = TTbarTrueFakePlot(norm, "mTW_GeV", "weight_new", (50, 40, 240) if region != "2" else (50, 140, 340))
drawStack(rwt_cn.nominalPlot(), "m_{T}^{W} [GeV]", regionTeX, f"forThesis/after/stack_mtw_fr_os" + suffix_syst, systs=rwt_cn.systematicPlots(), comp=norm_plt, ratio_range=ratrng)

print(rwt_cn.numberOfSysts())
rwt_cn.checkYields()
