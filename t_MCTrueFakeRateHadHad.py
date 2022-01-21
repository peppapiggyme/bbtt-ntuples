import ROOT as R
R.gROOT.SetBatch(True)
R.gROOT.SetStyle("ATLAS")
R.gStyle.SetErrorX(0.5)
R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")

import array
from analysis.utils import fakerates_mc, TermColor

"""
tau_truth
0  : true tau
1  : true electron
2  : true muon
3  : gluon
4  : d-quark
5  : u-quark
6  : s-quark
7  : c-quark
8  : b-quark
9  : others
"""

"""
TODO: 
- (?) tauSF should be saved in the ntuple, does it need to be removed from the weight
- (need new ntuple) the prescaled trigger matching info should be saved
"""

fout = R.TFile("rootfiles/MCTrueFakeHadHad.root", "RECREATE")

tau_truth_map = {
    0  : "T",
    1  : "E",
    2  : "M",
    3  : "G",
    4  : "D",
    5  : "U",
    6  : "S",
    7  : "C",
    8  : "B",
    9  : "O",
}

bin0 = array.array('d', [20, 25, 30, 35, 40, 45, 55, 70, 90, 1000])
bin1 = array.array('d', [30, 35, 40, 45, 55, 70, 100, 1000])
bin2 = array.array('d', [40, 45, 55, 70, 90, 1000])
bin3 = array.array('d', [20, 30, 40, 50, 70, 90, 1000])
bin4 = array.array('d', [30, 40, 50, 70, 90, 1000])
bin5 = array.array('d', [40, 50, 70, 90, 1000])

bin00 = {"1P": bin0, "3P": bin3}
bin25 = {"1P": bin1, "3P": bin4}
bin35 = {"1P": bin2, "3P": bin5}

period_15_18 = "rnd_run_number >= 266904 && rnd_run_number <= 364485"
period_18 = "rnd_run_number >= 348197 && rnd_run_number <= 364485"
period_18_fix = "rnd_run_number >= 350067 && rnd_run_number <= 364485"
period_18_K = "rnd_run_number >= 355529 && rnd_run_number <= 364485"

trig_map = {
    "25": [f"match_tau25 && {period_15_18}", period_15_18],
    "35": [f"match_tau35 && {period_15_18}", period_15_18],
    "25EF": [f"match_tau25_EF && {period_18}", period_18],
    "35EF": [f"match_tau35_EF && {period_18}", period_18],  # fix is only for data
    "25RNN": [f"match_tau25_RNN && {period_18_K}", period_18_K],
    "35RNN": [f"match_tau35_RNN && {period_18_K}", period_18_K],
}

def getMCTrueFakeRate(tauTruth, trigger, prong, all=False):
    region = "n_btag == 2 && n_jets >= 2 && same_sign == 0 && tau_truth > 2 && tau_truth < 10 && ttbar_tau_truth != 3 && pass_fr_sel"
    path = "../ResolvedNtuples/ntup-ttbar_noTrigger-fake-hadhad.root"
    df_total = R.RDataFrame("Nominal", path).Filter(region)
    df_total = df_total.Define("tau_ptGeV", "tau_pt / 1000.").Define("weight_new", "weight / tauSF")
    """
    add a criteria called *pass_fr_sel* because 
    total should be everything that starting at the CxAOD level (any bias here already?)
    passID should include the fake rate selections, e.g., passIDAndMatching, ...
    TODO: need to check it carefully
    """
    df_pasid = R.RDataFrame("Nominal", path).Filter(region + " && tau_loose")
    df_pasid = df_pasid.Define("tau_ptGeV", "tau_pt / 1000.").Define("weight_new", "weight")

    CharTauTruth = "X"
    if all:
        CharTauTruth = "A"
    else:
        CharTauTruth = tau_truth_map[tauTruth]

    print(f"{TermColor.OKBLUE}Calculating fake rates for TYPE [{CharTauTruth}], TRIGGER [{trigger}], PRONG [{prong}]... {TermColor.ENDC}")

    df_total = df_total.Filter(f"tau_prong == {prong[0]}")
    if not all: 
        df_total = df_total.Filter(f"tau_truth == {tauTruth}")
    if trigger:
        df_total = df_total.Filter(trig_map[trigger][1])
    
    df_pasid = df_pasid.Filter(f"tau_prong == {prong[0]}")
    if not all:
        df_pasid = df_pasid.Filter(f"tau_truth == {tauTruth}")
    if trigger:
        df_pasid = df_pasid.Filter(trig_map[trigger][0])

    h_total = df_total.Histo1D(R.RDF.TH1DModel("fake_ttbar", "tau_ptGeV", 980, 20, 1000), "tau_ptGeV", "weight_new")
    h_pasid = df_pasid.Histo1D(R.RDF.TH1DModel("fake_ttbar", "tau_ptGeV", 980, 20, 1000), "tau_ptGeV", "weight_new")
    
    binning_here = bin00[prong]
    if trigger:
        binning_here = bin25[prong] if "25" in trigger else bin35[prong]

    h_total = h_total.Rebin(len(binning_here) - 1, "fake_ttba_rebin", binning_here)
    h_pasid = h_pasid.Rebin(len(binning_here) - 1, "fake_ttba_rebin", binning_here)

    fm = fakerates_mc(h_pasid, h_total, trigger, prong)
    fm.SetName(f"fakerate_mc_{CharTauTruth}_trig{trigger}_{prong}")
    fm.SetTitle(f"fakerate_mc_{CharTauTruth}_trig{trigger}_{prong}")

    c = R.TCanvas("test", "test", 800, 600)
    fm.Draw()
    fout.cd()
    fm.Write()

    c.SaveAs(f"plots/test/c_MCTrueFakeRateHadHad_{CharTauTruth}_{trigger}_{prong}.png")

for prong in ["1P", "3P"]:
    for tauTruth in range(3, 10):
        getMCTrueFakeRate(tauTruth, None, prong, False)
        for trigger in ["25", "35", "25EF", "35EF", "25RNN", "35RNN"]:
            getMCTrueFakeRate(tauTruth, trigger, prong, False)

for prong in ["1P", "3P"]:
    getMCTrueFakeRate(42, None, prong, True)
    for trigger in ["25", "35", "25EF", "35EF", "25RNN", "35RNN"]:
        getMCTrueFakeRate(42, trigger, prong, True)

fout.Close()
