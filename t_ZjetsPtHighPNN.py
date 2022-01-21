
import ROOT as R
import os
import sys
from analysis.utils import *
from analysis.plot import *

filename_sr = "/scratchfs/atlas/bowenzhang/CxAODReaderForSystStudy/run/ntup-Ztautau.root"
filename_cr = "/afs/ihep.ac.cn/users/b/bowenzhang/public_store/ntuple/bbll_mva_210409_all/ZllCR/bbll.root"

cut_sr = "is_sr && !same_sign && n_btag == 2 && n_jets >= 2 && b0_truth_match >= 4 && b1_truth_match >= 4"

df_sr = R.RDataFrame("Nominal", filename_sr).Filter(cut_sr)
df_cr_mm = R.RDataFrame("Zmm_bb", filename_cr)
df_cr_ee = R.RDataFrame("Zee_bb", filename_cr)

# Last bins

h_PNN400  = df_sr.Filter("PNN400  > 0.5").Histo1D(R.RDF.TH1DModel("ptz_400",  "sherpaPtV", 1000, 0, 1000), "sherpaPtV", "weight")
h_PNN800 = df_sr.Filter("PNN800 > 0.5").Histo1D(R.RDF.TH1DModel("ptz_800", "sherpaPtV", 1000, 0, 1000), "sherpaPtV", "weight")
h_PNN1200 = df_sr.Filter("PNN1200 > 0.5").Histo1D(R.RDF.TH1DModel("ptz_1200", "sherpaPtV", 1000, 0, 1000), "sherpaPtV", "weight")
h_PNN1600 = df_sr.Filter("PNN1600 > 0.5").Histo1D(R.RDF.TH1DModel("ptz_1600", "sherpaPtV", 1000, 0, 1000), "sherpaPtV", "weight")
h_CR_mm = df_cr_mm.Histo1D(R.RDF.TH1DModel("ptll_CR_mm", "ll_pt", 1000, 0, 1000), "ll_pt", "weight")
h_CR_ee = df_cr_ee.Histo1D(R.RDF.TH1DModel("ptll_CR_ee", "ll_pt", 1000, 0, 1000), "ll_pt", "weight")
h_CR = h_CR_mm.Clone("ptll_CR")
h_clone = R.TH1D()
h_clone = h_CR_ee.Clone() 
h_CR.Add(h_clone)

c = R.TCanvas("test", "test", 800, 600)

h_PNN400.GetXaxis().SetTitle("True p_{T}^{Z}")
h_PNN400.GetYaxis().SetTitle("Normalised to 1.")

ALPHA = 0.2
REBIN = 20

h_PNN400.Rebin(REBIN)
h_PNN400.SetLineColor(R.kRed+1)
h_PNN400.SetFillColorAlpha(R.kRed+1, ALPHA)
h_PNN400.DrawNormalized("HIST SAME")
h_PNN800.Rebin(REBIN)
h_PNN800.SetLineColor(R.kOrange+1)
h_PNN800.SetFillColorAlpha(R.kOrange+1, ALPHA)
h_PNN800.DrawNormalized("HIST SAME")
h_PNN1200.Rebin(REBIN)
h_PNN1200.SetLineColor(R.kYellow+1)
h_PNN1200.SetFillColorAlpha(R.kYellow+1, ALPHA)
h_PNN1200.DrawNormalized("HIST SAME")
h_PNN1600.Rebin(REBIN)
h_PNN1600.SetLineColor(R.kGreen+1)
h_PNN1600.SetFillColorAlpha(R.kGreen+1, ALPHA)
h_PNN1600.DrawNormalized("HIST SAME")
h_CR.Rebin(REBIN)
h_CR.SetLineColor(R.kBlack)
h_CR.SetLineStyle(2)
h_CR.SetFillStyle(0)
h_CR.DrawNormalized("HIST SAME")

leg = R.TLegend(0.56, 0.60, 0.86, 0.90)
leg.SetTextFont(42)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
leg.SetTextSize(0.04)
leg.SetTextAlign(32)
leg.AddEntry("ptll_CR", "p_{T}^{#font[12]{ll}} in ZCR", "l")
leg.AddEntry("ptz_400", "PNN400 > 0.5", "lf")
leg.AddEntry("ptz_800", "PNN800 > 0.5", "lf")
leg.AddEntry("ptz_1200", "PNN1200 > 0.5", "lf")
leg.AddEntry("ptz_1600", "PNN1600 > 0.5", "lf")
leg.Draw("SAME")

text = R.TLatex()
text.SetNDC()
text.SetTextFont(72)
text.SetTextSize(0.045)
text.SetTextFont(42)
text.SetTextSize(0.040)
text.DrawLatex(0.56, 0.55, "Sherpa Z+hf samples")

c.SaveAs("ptv_CR_SR.pdf")


