import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

print(f"{TermColor.OKBLUE}Starting program ... {TermColor.ENDC}")

R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

rwt = AnaTTbarTrueFake(tauid=False, isOS=True)
rwt.add_var("ST_GeV", "ST / 1e3")
rwt_1bin = TTbarTrueFakePlot(rwt, "OS", "weight", (1, -100, 100))
norm = rwt_1bin.checkTTBarNorm()
rwt_1bin.checkEntries()
rwt.applyTauSFAndTTBarNorm("weight", "weight_norm")

regionTeX = "lephad, OS, Mbb>150, MTW>40, No #tau ID"

suffix_before = f"_before.pdf"
suffix_after = f"_after.pdf"

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

    binning_st = {}
    binning_st[2] = [0, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 3000]
    binning_st[3] = [0, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 3000]
    binning_st[4] = [0, 250, 300, 350, 400, 450, 500, 550, 600, 700, 800, 900, 3000]
    binning_st[5] = [0, 250, 300, 350, 400, 450, 500, 550, 600, 700, 800, 900, 1000, 3000]
    binning_st[6] = [0, 300, 350, 400, 450, 500, 550, 600, 650, 700, 800, 900, 1000, 3000]
    binning_st[7] = [0, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 3000]
    binning_st[8] = [0, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 3000]
    binning_st[9] = [0, 500, 700, 800, 900, 1100, 1400, 3000]
    binning_st[10] = [0, 700, 1000, 1200, 1500, 3000]

    rwt_st = TTbarTrueFakePlot(rwt, "ST_GeV", "weight_norm", (3000, 0, 3000), array.array('d', binning_st[i]))
    drawStack(rwt_st, "H_{T} [GeV]", regionTeX, f"plots/{i}jets/stack_st_fr_os" + suffix_before)
    
    print(f"{TermColor.OKBLUE}Yields (Before reweighting) {TermColor.ENDC}")
    
    # rwt_st.checkYields()

    reweight1D(rwt_st, "H_{T} [GeV]", f"plots/{i}jets/wt1d_st_fr_os_{i}.pdf", f"_{i}jets", 
        canvas_size=(1200,900), ytitle=f"t#bar{{t}} Reweight f(H_{{T}},{i})", hline=1, njets=f"{i}")

    # Apply reweighting
    # ------------------

    rwt.applyTauSFAndTTBarNormAndWeightNjets("weight", "weight_rw", ("ST_GeV", os.path.join(os.getcwd(), "include", f"Reweight1D_{i}jets.h")), f"_{i}jets")

    # After reweighting
    # ------------------

    rwt_st = TTbarTrueFakePlot(rwt, "ST_GeV", "weight_rw", (3000, 0, 3000), array.array('d', binning_st[i]))
    drawStack(rwt_st, "H_{T} [GeV]", regionTeX, f"plots/{i}jets/stack_st_fr_os" + suffix_after)

    rwt_njets = TTbarTrueFakePlot(rwt, "n_jets", "weight_rw", (11, 2, 13))
    drawStack(rwt_njets, "# jets", regionTeX, f"plots/{i}jets/stack_njets_fr_os" + suffix_after)

    print(f"{TermColor.OKBLUE}Yields (After reweighting) {TermColor.ENDC}")

    rwt_st.checkYields()

    print(f"{TermColor.OKGREEN}Finished njets = {i}! {TermColor.ENDC}")

print(f"{TermColor.OKGREEN}All n jets are done! {TermColor.ENDC}")
del rwt

rwt = AnaTTbarTrueFake(tauid=False, isOS=True)
rwt.add_var("ST_GeV", "ST / 1e3")

rwt_1bin = TTbarTrueFakePlot(rwt, "OS", "weight", (1, -100, 100))
print(f"{TermColor.OKBLUE}Yields (Before reweighting) {TermColor.ENDC}")
rwt_1bin.checkYields()
rwt_1bin.checkTTBarNorm()

rwt.applyTauSFAndTTBarNormAndWeightStep1("weight", "weight_rw", ("ST_GeV", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")))

rwt_1bin = TTbarTrueFakePlot(rwt, "OS", "weight_rw", (1, -100, 100))
print(f"{TermColor.OKBLUE}Yields (After reweighting step 1) {TermColor.ENDC}")
rwt_1bin.checkYields()
rwt_1bin.checkTTBarNorm()
