import ROOT as R
import os
import array
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

print(f"{TermColor.OKBLUE}Starting program ... {TermColor.ENDC}")

# current variation
# -----------------
# maybe this is the same as the ntuple tree name
#
current_variation = "Nominal"

print(f"{TermColor.OKBLUE}Defining numerator and denominator ... {TermColor.ENDC}")

# pass id
pasid = AnaTTbarTrueFake(tauid=True, isOS=True)
pasid.applyWeightStep1(
    ("HT", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")), True)
pasid.applyWeightStep2(
    ("dRbb", os.path.join(os.getcwd(), "include", "Reweight1D_dRbb.h")), True)
pasid.applyWeightStep3(
    ("dRTauLep", os.path.join(os.getcwd(), "include", "Reweight1D_dRlh.h")), True)

# no id
total = AnaTTbarTrueFake(tauid=False, isOS=True)
# False: already loaded in dynamic scope
total.applyWeightStep1(
    ("HT", os.path.join(os.getcwd(), "include", "Reweight1D_njets.h")), False)
total.applyWeightStep2(
    ("dRbb", os.path.join(os.getcwd(), "include", "Reweight1D_dRbb.h")), False)
total.applyWeightStep3(
    ("dRTauLep", os.path.join(os.getcwd(), "include", "Reweight1D_dRlh.h")), False)
print(f"{TermColor.OKGREEN}Done {TermColor.ENDC}")

# output root file
fout = R.TFile("rootfiles/ttbar-fakerates.root", "recreate")
fdir = fout.mkdir(current_variation)
fdir.cd()

# binnings
bin0 = array.array('d', [20000, 25000, 30000, 35000,
                         40000, 45000, 55000, 70000, 90000, 1000000])
bin1 = array.array('d', [30000, 35000, 40000, 45000,
                         55000, 70000, 100000, 1000000])
bin2 = array.array('d', [40000, 45000, 55000, 70000, 90000, 1000000])
bin3 = array.array('d', [20000, 30000, 40000, 50000, 70000, 90000, 1000000])
bin4 = array.array('d', [30000, 40000, 50000, 70000, 90000, 1000000])
bin5 = array.array('d', [40000, 50000, 70000, 90000, 1000000])

bin00 = {"1P": bin0, "3P": bin3}
bin25 = {"1P": bin1, "3P": bin4}
bin35 = {"1P": bin2, "3P": bin5}

print(f"{TermColor.OKBLUE}Calculating fake rates ... {TermColor.ENDC}")

period_15_17 = "rnd_run_number >= 266904 && rnd_run_number <= 341649"
period_18 = "rnd_run_number >= 348197 && rnd_run_number <= 364485"
period_18_K = "rnd_run_number >= 355529 && rnd_run_number <= 364485"

trig_map = {
    "25": [f"match_tau25 && {period_15_17}", period_15_17],
    "35": [f"match_tau35 && {period_15_17}", period_15_17],
    "25EF": [f"match_tau25_EF && {period_18}", period_18],
    "35EF": [f"match_tau35_EF && {period_18}", period_18],
    "25RNN": [f"match_tau25_RNN && {period_18_K}", period_18_K],
    "35RNN": [f"match_tau35_RNN && {period_18_K}", period_18_K],
}

for prong in ["1P", "3P"]:
    # offline ID fake rates
    # ---------------------
    print(
        f"{TermColor.OKBLUE}Prong={prong[0]}, calculating offline ID fake rates, using full dataset ...{TermColor.ENDC}")
    df_pasid_prong = {}
    df_total_prong = {}
    for p in pasid.processes:
        df_pasid_prong[p] = pasid.df[p].Filter(f"tau_prong == {prong[0]}")
        df_total_prong[p] = total.df[p].Filter(f"tau_prong == {prong[0]}")

    pasid.set_current_df(df_pasid_prong)
    total.set_current_df(df_total_prong)

    plot_pasid = TTbarTrueFakePlot(
        pasid, "tau_pt", "weight_new", (9800, 20000, 1000000), bin00[prong])
    plot_total = TTbarTrueFakePlot(
        total, "tau_pt", "weight_new", (9800, 20000, 1000000), bin00[prong])

    drawStack(plot_pasid, "#tau p_{T} [MeV]", f"lephad, OS, {prong}, offline ID",
              f"plots/tau_pt/stack_tau_pt_tauid_{prong}.pdf")
    drawStack(plot_total, "#tau p_{T} [MeV]", f"lephad, OS, {prong}, no ID",
              f"plots/tau_pt/stack_tau_pt_{prong}.pdf")

    fd, fm = fakerates(plot_pasid, plot_total, "00", prong)
    fd.Write()
    fm.Write()

    # offline + online ID fake rates
    # ------------------------------
    for trigger in ["25", "35", "25EF", "35EF", "25RNN", "35RNN"]:
        print(
            f"{TermColor.OKBLUE}Prong={prong[0]}, calculating offline + online({trigger}) ID fake rates ...{TermColor.ENDC}")
        df_pasid_trig = {}
        df_total_trig = {}
        for p in pasid.processes:
            df_pasid_trig[p] = df_pasid_prong[p].Filter(trig_map[trigger][0])
            df_total_trig[p] = df_total_prong[p].Filter(trig_map[trigger][1])

        pasid.set_current_df(df_pasid_trig)
        total.set_current_df(df_total_trig)

        binning_here = bin25[prong] if "25" in trigger else bin35[prong]

        plot_pasid = TTbarTrueFakePlot(
            pasid, "tau_pt", "weight_new", (9800, 20000, 1000000), binning_here)
        plot_total = TTbarTrueFakePlot(
            total, "tau_pt", "weight_new", (9800, 20000, 1000000), binning_here)

        drawStack(plot_pasid, "#tau p_{T} [MeV]", f"lephad, OS, {prong}, offline ID + HLT_tau{trigger}",
                  f"plots/tau_pt/stack_tau_pt_tauid_{prong}_{trigger}.pdf")
        # the trigger is in the filename but only year cut is applied not trigger matching to the denominator
        drawStack(plot_total, "#tau p_{T} [MeV]", f"lephad, OS, {prong}, no ID",
                  f"plots/tau_pt/stack_tau_pt_{prong}_{trigger}.pdf")

        fd, fm = fakerates(plot_pasid, plot_total, trigger, prong)
        fd.Write()
        fm.Write()

print(f"{TermColor.OKGREEN}All done!{TermColor.ENDC}")

pasid.set_current_df(pasid.df)
total.set_current_df(total.df)

fout.Close()
print(f"{TermColor.OKGREEN}Output file closed{TermColor.ENDC}")
