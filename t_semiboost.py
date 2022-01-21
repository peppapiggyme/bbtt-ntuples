
import ROOT as R
import os
import sys
from analysis.utils import *
from analysis.plot import *

masses = ["1000", "1200", "1400", "1600", "1800", "2000"]

cut_sr = "is_sr && !same_sign && n_btag == 2"

variables = [
    ("MET", 50, 0, 500 * 1e3),
    ("mBB", 50, 0, 250 * 1e3),
    ("mHH", 50, 500, 1500 * 1e3),
    # ("b0_m", 50, 0, 250),
    # ("b1_m", 50, 0, 250),
    ("dRBB", 50, 0, 2.5),
    ("mMMC", 50, 60, 160 * 1e3),
    ("pTBB", 50, 0, 1000 * 1e3),
    ("pTHH", 50, 0, 1000 * 1e3),
    ("SMBDT", 50, -1, 1),
    ("b0_pt", 50, 0, 500 * 1e3),
    ("b1_pt", 50, 0, 500 * 1e3),
    ("PNN800", 50, 0, 1),
    ("PNN900", 50, 0, 1),
    # ("b0_eta", 1000, 0, 1000),
    # ("b0_phi", 1000, 0, 1000),
    # ("b1_eta", 1000, 0, 1000),
    # ("b1_phi", 1000, 0, 1000),
    ("mmc_pt", 50, 0, 1000 * 1e3),
    # ("MET_phi", 1000, 0, 1000),
    ("PNN1000", 50, 0, 1),
    ("PNN1100", 50, 0, 1),
    ("PNN1200", 50, 0, 1),
    ("PNN1400", 50, 0, 1),
    ("PNN1600", 50, 0, 1),
    # ("mmc_eta", 1000, 0, 1000),
    # ("mmc_phi", 1000, 0, 1000),
    ("tau0_pt", 50, 0, 500 * 1e3),
    ("tau1_pt", 50, 0, 500 * 1e3),
    ("dRTauTau", 50, 0, 2.5),
    ##("fatjet_m", 50, 0, 250),
    ("pTTauTau", 50, 0, 1000 * 1e3),
    # ("tau0_eta", 1000, 0, 1000),
    # ("tau0_phi", 1000, 0, 1000),
    # ("tau1_eta", 1000, 0, 1000),
    # ("tau1_phi", 1000, 0, 1000),
    ##("fatjet_pt", 50, 0, 1000),
    ("dPhiHbbMET", 50, -4, 4),
    # ("fatjet_eta", 1000, 0, 1000),
    # ("fatjet_phi", 1000, 0, 1000),
]

def run(mass):
    filename_resolved = \
        "/scratchfs/atlas/bowenzhang/CxAODReaderSemiBoosted/run/ntuples/resonant-resolved/Xtohh{}-0.root".format(mass)
    # filename_semiboosted = \
    #     "/scratchfs/atlas/bowenzhang/CxAODReaderSemiBoosted/run/ntuples/resonant-semiboosted/deco-{}.root".format(mass)
    filename_semiboosted = \
        "/scratchfs/atlas/bowenzhang/CxAODReaderSemiBoosted/run/ntuples/resonant-semiboosted-skipjetptcut/deco-{}.root".format(mass)

    df_resolved = R.RDataFrame("Nominal", filename_resolved).Filter(cut_sr)
    df_semiboosted = R.RDataFrame("Nominal", filename_semiboosted).Filter(cut_sr)
    df_semiboosted_recover = R.RDataFrame("Nominal", filename_semiboosted).Filter(cut_sr + " && isSelectedByResolved == 0")

    for var, nbins, xstart, xend in variables:
        c = R.TCanvas(var, var, 800, 600)
        
        h_resolved = df_resolved.Histo1D(R.RDF.TH1DModel(var+"_resolved", var, nbins, xstart, xend), var, "weight")
        h_semiboosted = df_semiboosted.Histo1D(R.RDF.TH1DModel(var+"_semiboosted", var, nbins, xstart, xend), var, "weight")
        h_semiboosted_recover = df_semiboosted_recover.Histo1D(R.RDF.TH1DModel(var+"_semiboosted_recover", var, nbins, xstart, xend), var, "weight")
        h_resolved.GetXaxis().SetTitle(var)
        h_resolved.GetYaxis().SetTitle("# events")
        h_resolved.SetLineWidth(2)
        h_resolved.SetLineColor(R.kBlack)
        h_semiboosted.SetLineWidth(2)
        h_semiboosted.SetLineColor(R.kBlue)
        h_semiboosted_recover.SetLineWidth(2)
        h_semiboosted_recover.SetLineColor(R.kCyan)
        h_semiboosted_recover.SetFillColorAlpha(R.kCyan, 0.2)

        if var == "SMBDT":
            # show yields
            n_resolved = h_resolved.Integral()
            n_semiboosted = h_semiboosted.Integral()
            n_semiboosted_recover = h_semiboosted_recover.Integral()
            print("Mass = {}".format(mass))
            print("- n_res = {}".format(n_resolved))
            print("- n_sem = {}".format(n_semiboosted))
            print("- n_recover (rate) = {} ({})".format(n_semiboosted_recover, n_semiboosted_recover / n_semiboosted))
        
        h_resolved.Draw("HIST")
        h_semiboosted.Draw("HIST SAME")
        h_semiboosted_recover.Draw("HIST SAME")

        leg = R.TLegend(0.60, 0.70, 0.90, 0.90)
        leg.SetTextFont(42)
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        leg.SetTextSize(0.032)
        leg.SetTextAlign(32)
        leg.AddEntry(h_resolved.GetName(), "Resolved", "l")
        leg.AddEntry(h_semiboosted.GetName(), "Semi-boosted (SB)", "l")
        leg.AddEntry(h_semiboosted_recover.GetName(), "Recovered by SB", "lf")
        leg.Draw("SAME")

        c.SaveAs("/scratchfs/atlas/bowenzhang/bbtt-ntuples/plots/semiboost-skipjetptcut/semiboost-{}-{}.png".format(mass, var))

for m in masses:
    run(m)