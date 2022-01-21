"""
Fill histograms using bbll ntuples
"""

import ROOT as R
import os
from analysis.utils import *
from analysis.ana import *
from analysis.plot import *

region = "ZllCR"

var_list = {
    ("ll_m", 244, -10, 600, "mMMC"),
    ("ll_deltar", 100, 0, 5, "dRTauTau"),
    ("bb_m", 200, 0, 500, "mBB"),
    ("bb_deltar", 100, 0, 5, "dRBB"),
    ("met_met", 100, 0, 5, "MET"),
    ("lept_0_pt", 100, 0, 250, "Tau0Pt"),
    ("lept_1_pt", 100, 0, 250, "Tau1Pt"),
    ("bjet_0_pt", 200, 0, 250, "pTB0"),
    ("bjet_1_pt", 200, 0, 250, "pTB1"),
    ("ht", 50, 0, 1000, "HT"),
    ("st", 70, 0, 1400, "sTAll"),
}

def reader_hist_name(var):
    r"""
    Can merge preselection dir    
    LepHad + HadHad + ZhfCR
    Then all can be done in bbtautau-hists
    Hack: difference is process name
    Call it ttbarFromZCR
    """
    return "_".join(["ttbarFromZCR", "2tag2pjet_0ptv_LL_OS", var])

bbll = AnaBBLL(rewrite="1", 
               path="/publicfs/atlas/atlasnew/higgs/hh2X/zhangbw/ntuple/bbll_mva_210409/ZllCR_v2/")

ttbar = bbll.df["ttbarIncl"]
ttbar = ttbar.Define("st", "ht + lept_0_pt + lept_1_pt + met_met")

f = R.TFile("bbll_output/hist-ttbar-bbll-{}.root".format(region), "recreate")
d = f.mkdir("Preselection")
d.cd()

for v in var_list:
    h = ttbar.Histo1D(R.RDF.TH1DModel(reader_hist_name(v[-1]), v[0], v[1], v[2], v[3]), v[0], "weight")
    h.SetDirectory(d)
    h.Write()

f.Close()
