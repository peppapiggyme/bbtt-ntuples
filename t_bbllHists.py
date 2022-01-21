"""
Fill histograms using bbll ntuples

Improve parallism of histogram filling
"""

import ROOT as R
import os
import sys
import multiprocessing, signal
from analysis.utils import *
from analysis.plot import *

# region = "SR2"
region = "ZllCR"
tag = sys.argv[1]

var_list = {
#    ("mHHGeV", 1600, 0, 1600, "mHH"),
 #   ("PNN251", 1000, 0, 1, "PNN251"),
  #  ("PNN260", 1000, 0, 1, "PNN260"),
   # ("PNN280", 1000, 0, 1, "PNN280"),
#    ("PNN300", 1000, 0, 1, "PNN300"),
 #   ("PNN325", 1000, 0, 1, "PNN325"),
  #  ("PNN350", 1000, 0, 1, "PNN350"),
   # ("PNN375", 1000, 0, 1, "PNN375"),
#    ("PNN400", 1000, 0, 1, "PNN400"),
 #   ("PNN450", 1000, 0, 1, "PNN450"),
  #  ("PNN500", 1000, 0, 1, "PNN500"),
   # ("PNN550", 1000, 0, 1, "PNN550"),
#    ("PNN600", 1000, 0, 1, "PNN600"),
 #   ("PNN700", 1000, 0, 1, "PNN700"),
  #  ("PNN800", 1000, 0, 1, "PNN800"),
   # ("PNN900", 1000, 0, 1, "PNN900"),
   # ("PNN1000", 1000, 0, 1, "PNN1000"),
   # ("PNN1200", 1000, 0, 1, "PNN1200"),
   # ("PNN1400", 1000, 0, 1, "PNN1400"),
   # ("PNN1600", 1000, 0, 1, "PNN1600"),
   # ("SMBDT", 1000, 0, 1, "SMBDT"),
    ("ll_m", 500, 0, 500, "mMMC"),
    ("ll_pt", 1000, 0, 1000, "pTTauTau"),
    ("ll_m", 500, 0, 500, "mMMC"),
    ("ll_deltar", 100, 0, 5, "dRTauTau"),
    ("bb_pt", 1000, 0, 1000, "pTBB"),
    ("bb_m", 200, 0, 500, "mBB"),
    ("bb_deltar", 100, 0, 5, "dRBB"),
    ("met_met", 100, 0, 250, "MET"),
    ("lept_0_pt", 100, 0, 250, "Tau0Pt"),
    ("lept_1_pt", 100, 0, 250, "Tau1Pt"),
    ("bjet_0_pt", 200, 0, 250, "pTB0"),
    ("bjet_1_pt", 200, 0, 250, "pTB1"),
}

def reader_hist_name(process, var):
    r"""
    Can merge preselection dir    
    LepHad + HadHad + ZhfCR
    Then all can be done in bbtautau-hists
    Hack: difference is process name
    Call it ttbarFromZCR
    """
    return "_".join([process, "2tag2pjet_0ptv_LL_OS", var])

filename = "~/public_store/ntuple/bbll_mva_210409_all/ZllCR/bbll.root"

processes = [
#   ("sig_res_1000_bbww", "hhwwbb"),
#   ("sig_res_1000_bbzz", "hhzzbb"),
#   ("sig_res_1000_bbtautau", "hhttbb"),
  ("higgs_tautau_ggf", "ggFHtautau"),
  ("higgs_tautau_vbf", "VBFHtautau"),
  ("higgs_tautau_vh", "VHtautau"),
  ("higgs_ww_ggf", "ggFHWW"),
  ("higgs_ww_vbf", "VBFHWW"),
  ("higgs_ww_wh", "VHWW"),
  ("higgs_zz_ggf", "ggFHZZ"),
  ("higgs_zz_vbf", "VBFHZZ"),
  ("higgs_bb_zh", "ZHbb"),
  ("higgs_bb_ggf", "ggFHbb"),
  ("higgs_vh_wh", "WH"),
  ("higgs_vh_zh", "ZH"),
  ("higgs_tth", "ttH"),
  ("Zee_ll", "Zeell"),
  ("Zee_cc", "Zeecc"),
  ("Zee_bb", "Zeebb"),
  ("Zee_lowmass_llcc", "ZeeLowllcc"),
  ("Zee_lowmass_bb", "ZeeLowbb"),
  ("Zee_ew", "ZeeEW"),
  ("Zmm_ll", "Zmmll"),
  ("Zmm_cc", "Zmmcc"),
  ("Zmm_bb", "Zmmbb"),
  ("Zmm_lowmass_llcc", "ZmmLowllcc"),
  ("Zmm_lowmass_bb", "ZmmLowbb"),
  ("Zmm_ew", "ZmmEW"),
  ("Ztt", "Ztt"),
  ("diboson", "diboson"),
  ("fakes_Wenu", "FakeWenu"),
  ("fakes_Wmunu", "FakeWmunu"),
  ("fakes_Wtaunu", "FakeWtaunu"),
  ("fakes_diboson", "Fakediboson"),
  ("fakes_top_stop", "Fakestop"),
  ("fakes_top_ttbar", "Fakettbar"),
  ("stop", "stop"),
  ("ttbar", "ttbar"),
  ("ttbarV", "ttV"),
  ("data", "data"),
]

cuts = {
    "0716-LR": "ll_m > 85. && ll_m < 97. && ll_deltar < 1.5 && ((bb_m > 60. && bb_m < 95.) || (bb_m > 135. && bb_m < 160.)) && met_met < 45.",
    "0716-Left": "ll_m > 85. && ll_m < 97. && ll_deltar < 1.5 && ((bb_m > 60. && bb_m < 95.)) && met_met < 45.",
    "0716-Right": "ll_m > 85. && ll_m < 97. && ll_deltar < 1.5 && ((bb_m > 135. && bb_m < 160.)) && met_met < 45.",
    "0715": "ll_m > 85. && ll_m < 97. && ll_deltar < 1.5 && ((bb_m > 50. && bb_m < 150.)) && met_met < 45.",
    "0917": "ll_m < 110. && ll_m > 70. && (bb_m < 40. || bb_m > 210.)",
}

dframes = dict()

# print(cuts[tag])

for proc, _ in processes:
    # mll_cut
    dframes[proc] = R.RDataFrame(proc, filename) #\
        # .Define("ZJETS_GEN__1up", "weight * (0.547686 + 0.00357737 * (bb_m > 250. ? 250. : bb_m))") \
        # .Define("ZJETS_GEN__1down", "2. * weight - ZJETS_GEN__1up") \
        # .Define("ZJETS_NORM__1up", "weight * 1.1") \
        # .Define("ZJETS_NORM__1down", "weight * 0.9") \
        # .Define("ZJETS_XSEC__1up", "weight * 1.05") \
        # .Define("ZJETS_XSEC__1down", "weight * 0.95") \
        # .Define("mHHGeV", "mHH / 1e3") \
        # .Filter(cuts[tag])
        # .Filter("ll_m > 85. && ll_m < 97. && ll_deltar < 1.5 && ((bb_m > 60. && bb_m < 95.) || (bb_m > 135. && bb_m < 160.)) && met_met < 45.") # 0716-LR
        # .Filter("ll_m > 85. && ll_m < 97. && ll_deltar < 1.5 && ((bb_m > 50. && bb_m < 150.)) && met_met < 45.") # 0715
        # .Filter("ll_m > 85. && ll_m < 97. && ll_deltar < 1.5 && ((bb_m > 135. && bb_m < 160.)) && met_met < 45.") # 0716-Right
        # .Filter("ll_m > 85. && ll_m < 97. && ll_deltar < 1.5 && ((bb_m > 60. && bb_m < 95.)) && met_met < 45.") # 0716-Left
        # .Define("distance", "TMath::Abs(TVector2::Phi_mpi_pi(0.5*(bjet_0_phi+bjet_1_phi)-0.5*(lept_0_phi+lept_1_phi)))") \
    # mll_dR_cut
    # dframes[proc] = R.RDataFrame(proc, filename).Filter("ll_m > 85. && ll_m < 97. && ll_deltar + bb_deltar < 3")
    # dframes[proc] = R.RDataFrame(proc, filename).Filter("ll_m > 85. && ll_m < 97. && ll_deltar + bb_deltar < 3")
    # dframes[proc] = R.RDataFrame(proc, filename)

f = R.TFile("bbll_output/hist-ttbar-bbll-{}-{}.root".format(region, tag), "recreate")
d = f.mkdir("Preselection")
d.cd()

print("\n\nNominal\n\n")

def main_helper(v, proc, proc_name):
    print(v, proc_name)
    h = dframes[proc].Histo1D(R.RDF.TH1DModel(reader_hist_name(proc_name, v[-1]), v[0], v[1], v[2], v[3]), v[0], "weight")
    h.SetDirectory(d)
    h.Write()

for proc, proc_name in processes:
    for v in var_list:
        main_helper(v, proc, proc_name)


# print("\n\nVariations\n\n")
# d_syst = d.mkdir("Systematics")
# d_syst.cd()

# for v in var_list:
#     for proc, proc_name in processes:
#         if proc in {"Zee_bb", "Zee_lowmass_bb", "Zmm_bb", "Zmm_lowmass_bb"}:
#             print(v, proc_name)
#             hUp_1 = dframes[proc].Histo1D(R.RDF.TH1DModel(reader_hist_name(proc_name, v[-1] + "_SysZJETS_GEN__1up"), v[0], v[1], v[2], v[3]), v[0], "ZJETS_GEN__1up")
#             hDo_1 = dframes[proc].Histo1D(R.RDF.TH1DModel(reader_hist_name(proc_name, v[-1] + "_SysZJETS_GEN__1down"), v[0], v[1], v[2], v[3]), v[0], "ZJETS_GEN__1down")
#             hUp_2 = dframes[proc].Histo1D(R.RDF.TH1DModel(reader_hist_name(proc_name, v[-1] + "_SysZJETS_NORM__1up"), v[0], v[1], v[2], v[3]), v[0], "ZJETS_NORM__1up")
#             hDo_2 = dframes[proc].Histo1D(R.RDF.TH1DModel(reader_hist_name(proc_name, v[-1] + "_SysZJETS_NORM__1down"), v[0], v[1], v[2], v[3]), v[0], "ZJETS_NORM__1down")
#             hUp_3 = dframes[proc].Histo1D(R.RDF.TH1DModel(reader_hist_name(proc_name, v[-1] + "_SysZJETS_XSEC__1up"), v[0], v[1], v[2], v[3]), v[0], "ZJETS_XSEC__1up")
#             hDo_3 = dframes[proc].Histo1D(R.RDF.TH1DModel(reader_hist_name(proc_name, v[-1] + "_SysZJETS_XSEC__1down"), v[0], v[1], v[2], v[3]), v[0], "ZJETS_XSEC__1down")
#             hUp_1.SetDirectory(d_syst)
#             hDo_1.SetDirectory(d_syst)
#             hUp_2.SetDirectory(d_syst)
#             hDo_2.SetDirectory(d_syst)
#             hUp_3.SetDirectory(d_syst)
#             hDo_3.SetDirectory(d_syst)
#             hUp_1.Write()
#             hDo_1.Write()
#             hUp_2.Write()
#             hDo_2.Write()
#             hUp_3.Write()
#             hDo_3.Write()

f.Close()
