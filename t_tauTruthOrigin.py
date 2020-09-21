import ROOT as R
R.gROOT.SetBatch(True)
R.gROOT.SetStyle("ATLAS")
R.gStyle.SetErrorX(0.5)
import random

# ptbin_hh = "&& otherTau_pt > 40000 && fakeTau_pt > 30000 && b0_pt > 45000 && b1_pt > 45000"
# ptbin_lh = "&& lep_pt > 40000 && tau_pt > 30000 && b0_pt > 45000 && b1_pt > 45000"

# name : [lephadCut, hadhadCut]
ptbins = {"all" : ["&& tau_pt > 20000 && tau_pt < 200000", "&& fakeTau_pt > 20000 && fakeTau_pt < 200000"]}

for iLow, iUp in [(20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (50, 55), (55, 60), (60, 65), (65, 70), (70, 75), (75, 80), (80, 90), (90, 120), (120, 160)]:
    ptbins[f"{iLow}-{iUp}"] = [f"&& tau_pt > {iLow}000 && tau_pt < {iUp}000", f"&& fakeTau_pt > {iLow}000 && fakeTau_pt < {iUp}000"]

# true-true
# ---------

def TT(ptbin_name, ptbin_lh, ptbin_hh):
    region = "n_btag == 2 && n_jets >= 2 && same_sign == 0 && tauTruth == 0 && is_sr" + ptbin_hh
    path = "../ttt-ntuple-v3/ttt-hh-withTrig.root"
    df_hadhad = R.RDataFrame("Nominal", path).Filter(region)

    region = "n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 80000.)) && mTW > 60000. && OS && !is_fake && tau_loose" + ptbin_lh
    path = "../ttt-ntuple-v3/ttt-lh.root"
    df_lephad = R.RDataFrame("Nominal", path).Filter(region)
    #df_lephad = df_lephad.Define("weight_new", "weight / tauSF")

    for i, pairs in enumerate([("otherTau_origin", "lep_origin"), ("fakeTau_origin", "tau_origin")]):
        c = R.TCanvas(f"c", "", 900, 900)
        h_hadhad = df_hadhad.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[0], "weight").GetValue()
        h_lephad = df_lephad.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[1], "weight").GetValue()

        h_hadhad.SetLineColor(R.kRed)
        h_hadhad.SetMarkerColor(R.kRed)
        h_lephad.SetLineColor(R.kBlue)
        h_lephad.SetMarkerColor(R.kBlue)

        h_hadhad.Scale(1.0 / h_hadhad.Integral())
        h_lephad.Scale(1.0 / h_lephad.Integral())

        tr = R.TRatioPlot(h_hadhad, h_lephad)
        tr.SetH1DrawOpt("HIST E1 SAME")
        tr.SetH2DrawOpt("HIST E1 SAME")
        tr.Draw()
        
        tr.GetUpperRefYaxis().SetRangeUser(0.0, 1.0)
        tr.GetLowerRefYaxis().SetRangeUser(0.0, 2.0)
        tr.GetLowYaxis().SetNdivisions(505)

        # ?
        tr.GetXaxis().SetBinLabel(1, "Others")
        tr.GetXaxis().SetBinLabel(2, "top->W")
        tr.GetXaxis().SetBinLabel(3, "top->b")

        text = R.TLatex()
        text.SetNDC()
        text.SetTextFont(72)
        text.SetTextSize(0.045)
        text.SetTextFont(42)
        text.SetTextSize(0.040)
        text.DrawLatex(0.46, 0.95, f"TT, p_T bin: {ptbin_name}, Obj: {i}")
        
        leg = R.TLegend(0.66, 0.60, 0.86, 0.75)
        leg.SetTextFont(42)
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        leg.SetTextSize(0.04)
        leg.SetTextAlign(32)
        leg.AddEntry(h_hadhad, "hadhad", "lep")
        leg.AddEntry(h_lephad, "lephad", "lep")
        leg.Draw("SAME")

        c.SaveAs(f"plots/test/hist_trueTTBar_TT_passID_{ptbin_name}_{i}.pdf")


# true-fake
# ---------

def TF(ptbin_name, ptbin_lh, ptbin_hh):
    region = "n_btag == 2 && n_jets >= 2 && same_sign == 0 && tauTruth == 1" + ptbin_hh
    path = "../ttt-ntuple-v3/ttt-hh-noTrig.root"

    print(region)
    df_hadhad = R.RDataFrame("Nominal", path).Filter(region)

    region = "n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 60000. && OS && is_fake" + ptbin_lh
    path = "../ttt-ntuple-v3/ttt-lh.root"

    print(region)
    df_lephad = R.RDataFrame("Nominal", path).Filter(region)
    df_lephad = df_lephad.Define("weight_new", "weight / tauSF")

    for i, pairs in enumerate([("otherTau_origin", "lep_origin"), ("fakeTau_origin", "tau_origin")]):
        c = R.TCanvas(f"c", "", 900, 900)
        h_hadhad = df_hadhad.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[0], "weight").GetValue()
        h_lephad = df_lephad.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[1], "weight_new").GetValue()

        h_hadhad.SetLineColor(R.kRed)
        h_hadhad.SetMarkerColor(R.kRed)
        h_lephad.SetLineColor(R.kBlue)
        h_lephad.SetMarkerColor(R.kBlue)

        h_hadhad.Scale(1.0 / h_hadhad.Integral())
        h_lephad.Scale(1.0 / h_lephad.Integral())

        tr = R.TRatioPlot(h_hadhad, h_lephad)
        tr.SetH1DrawOpt("HIST E1 SAME")
        tr.SetH2DrawOpt("HIST E1 SAME")
        tr.Draw()
        
        tr.GetUpperRefYaxis().SetRangeUser(0.0, 1.0)
        tr.GetLowerRefYaxis().SetRangeUser(0.0, 2.0)
        tr.GetLowYaxis().SetNdivisions(505)

        # ?
        tr.GetXaxis().SetBinLabel(1, "Others")
        tr.GetXaxis().SetBinLabel(2, "top->W")
        tr.GetXaxis().SetBinLabel(3, "top->b")

        text = R.TLatex()
        text.SetNDC()
        text.SetTextFont(72)
        text.SetTextSize(0.045)
        text.SetTextFont(42)
        text.SetTextSize(0.040)
        text.DrawLatex(0.46, 0.95, f"TF, p_T bin: {ptbin_name}, Obj: {i}")
        
        leg = R.TLegend(0.66, 0.60, 0.86, 0.75)
        leg.SetTextFont(42)
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        leg.SetTextSize(0.04)
        leg.SetTextAlign(32)
        leg.AddEntry(h_hadhad, "hadhad", "lep")
        leg.AddEntry(h_lephad, "lephad", "lep")
        leg.Draw("SAME")

        c.SaveAs(f"plots/test/hist_fakeTTBar_TF_noIDnoTrig_{ptbin_name}_{i}.pdf")


# fake-true
# ---------

def FT(ptbin_name, ptbin_lh, ptbin_hh):
    region = "n_btag == 2 && n_jets >= 2 && same_sign == 0 && tauTruth == 2" + ptbin_hh
    path = "../ttt-ntuple-v3/ttt-hh-noTrig.root"
    df_hadhad = R.RDataFrame("Nominal", path).Filter(region)

    region = "n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 60000. && OS && is_fake" + ptbin_lh
    path = "../ttt-ntuple-v3/ttt-lh.root"
    df_lephad = R.RDataFrame("Nominal", path).Filter(region)
    df_lephad = df_lephad.Define("weight_new", "weight / tauSF")

    for i, pairs in enumerate([("otherTau_origin", "lep_origin"), ("fakeTau_origin", "tau_origin")]):
        c = R.TCanvas(f"c", "", 900, 900)
        h_hadhad = df_hadhad.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[0], "weight").GetValue()
        h_lephad = df_lephad.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[1], "weight_new").GetValue()

        h_hadhad.SetLineColor(R.kRed)
        h_hadhad.SetMarkerColor(R.kRed)
        h_lephad.SetLineColor(R.kBlue)
        h_lephad.SetMarkerColor(R.kBlue)

        h_hadhad.Scale(1.0 / h_hadhad.Integral())
        h_lephad.Scale(1.0 / h_lephad.Integral())

        tr = R.TRatioPlot(h_hadhad, h_lephad)
        tr.SetH1DrawOpt("HIST E1 SAME")
        tr.SetH2DrawOpt("HIST E1 SAME")
        tr.Draw()

        tr.GetUpperRefYaxis().SetRangeUser(0.0, 1.0)
        tr.GetLowerRefYaxis().SetRangeUser(0.0, 2.0)
        tr.GetLowYaxis().SetNdivisions(505)

        # ?
        tr.GetXaxis().SetBinLabel(1, "Others")
        tr.GetXaxis().SetBinLabel(2, "top->W")
        tr.GetXaxis().SetBinLabel(3, "top->b")

        text = R.TLatex()
        text.SetNDC()
        text.SetTextFont(72)
        text.SetTextSize(0.045)
        text.SetTextFont(42)
        text.SetTextSize(0.040)
        text.DrawLatex(0.46, 0.95, f"FT, p_T bin: {ptbin_name}, Obj: {i}")
        
        leg = R.TLegend(0.66, 0.60, 0.86, 0.75)
        leg.SetTextFont(42)
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        leg.SetTextSize(0.04)
        leg.SetTextAlign(32)
        leg.AddEntry(h_hadhad, "hadhad", "lep")
        leg.AddEntry(h_lephad, "lephad", "lep")
        leg.Draw("SAME")

        c.SaveAs(f"plots/test/hist_fakeTTBar_FT_noIDnoTrig_{ptbin_name}_{i}.pdf")


# fake-fake
# ---------

def FF(ptbin_name, ptbin_lh, ptbin_hh):
    region = "n_btag == 2 && n_jets >= 2 && same_sign == 0 && tauTruth == 3" + ptbin_hh
    path = "../ttt-ntuple-v3/ttt-hh-noTrig.root"
    df_hadhad = R.RDataFrame("Nominal", path).Filter(region)

    region = "n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 60000. && OS && is_fake" + ptbin_lh
    path = "../ttt-ntuple-v3/ttt-lh.root"
    df_lephad = R.RDataFrame("Nominal", path).Filter(region)
    df_lephad = df_lephad.Define("weight_new", "weight / tauSF")

    for i, pairs in enumerate([("otherTau_origin", "lep_origin"), ("fakeTau_origin", "tau_origin")]):
        c = R.TCanvas(f"c", "", 900, 900)
        h_hadhad = df_hadhad.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[0], "weight").GetValue()
        h_lephad = df_lephad.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[1], "weight_new").GetValue()

        h_hadhad.SetLineColor(R.kRed)
        h_hadhad.SetMarkerColor(R.kRed)
        h_lephad.SetLineColor(R.kBlue)
        h_lephad.SetMarkerColor(R.kBlue)

        h_hadhad.Scale(1.0 / h_hadhad.Integral())
        h_lephad.Scale(1.0 / h_lephad.Integral())

        tr = R.TRatioPlot(h_hadhad, h_lephad)
        tr.SetH1DrawOpt("HIST E1 SAME")
        tr.SetH2DrawOpt("HIST E1 SAME")
        tr.Draw()
        
        tr.GetUpperRefYaxis().SetRangeUser(0.0, 1.0)
        tr.GetLowerRefYaxis().SetRangeUser(0.0, 2.0)
        tr.GetLowYaxis().SetNdivisions(505)

        # ?
        tr.GetXaxis().SetBinLabel(1, "Others")
        tr.GetXaxis().SetBinLabel(2, "top->W")
        tr.GetXaxis().SetBinLabel(3, "top->b")

        text = R.TLatex()
        text.SetNDC()
        text.SetTextFont(72)
        text.SetTextSize(0.045)
        text.SetTextFont(42)
        text.SetTextSize(0.040)
        text.DrawLatex(0.46, 0.95, f"FF, p_T bin: {ptbin_name}, Obj: {i}")
        
        leg = R.TLegend(0.66, 0.60, 0.86, 0.75)
        leg.SetTextFont(42)
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        leg.SetTextSize(0.04)
        leg.SetTextAlign(32)
        leg.AddEntry(h_hadhad, "hadhad", "lep")
        leg.AddEntry(h_lephad, "lephad", "lep")
        leg.Draw("SAME")

        c.SaveAs(f"plots/test/hist_fakeTTBar_FF_noIDnoTrig_{ptbin_name}_{i}.pdf")


# OS-SS lephad
# ------------

def OS_SS(ptbin_name, ptbin_lh, ptbin_hh):

    OS = "n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 60000. && OS && is_fake" + ptbin_lh
    SS = "n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 60000. && !OS && is_fake" + ptbin_lh
    path = "../ttt-ntuple-v3/ttt-lh.root"

    df_OS = R.RDataFrame("Nominal", path).Filter(OS)
    df_OS = df_OS.Define("weight_new", "weight / tauSF")

    df_SS = R.RDataFrame("Nominal", path).Filter(SS)
    df_SS = df_SS.Define("weight_new", "weight / tauSF")

    for i, pairs in enumerate([("lep_origin", "lep_origin"), ("tau_origin", "tau_origin")]):
        c = R.TCanvas(f"c", "", 900, 900)
        h_OS = df_OS.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[0], "weight_new").GetValue()
        h_SS = df_SS.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[1], "weight_new").GetValue()

        h_OS.SetLineColor(R.kRed)
        h_OS.SetMarkerColor(R.kRed)
        h_SS.SetLineColor(R.kBlue)
        h_SS.SetMarkerColor(R.kBlue)

        h_OS.Scale(1.0 / h_OS.Integral())
        h_SS.Scale(1.0 / h_SS.Integral())

        tr = R.TRatioPlot(h_OS, h_SS)
        tr.SetH1DrawOpt("HIST E1 SAME")
        tr.SetH2DrawOpt("HIST E1 SAME")
        tr.Draw()
        
        tr.GetUpperRefYaxis().SetRangeUser(0.0, 1.0)
        tr.GetLowerRefYaxis().SetRangeUser(0.0, 2.0)
        tr.GetLowYaxis().SetNdivisions(505)

        # ?
        tr.GetXaxis().SetBinLabel(1, "Others")
        tr.GetXaxis().SetBinLabel(2, "top->W")
        tr.GetXaxis().SetBinLabel(3, "top->b")

        text = R.TLatex()
        text.SetNDC()
        text.SetTextFont(72)
        text.SetTextSize(0.045)
        text.SetTextFont(42)
        text.SetTextSize(0.040)
        text.DrawLatex(0.46, 0.95, f"OS_SS, p_T bin: {ptbin_name}, Obj: {i}")
        
        leg = R.TLegend(0.66, 0.60, 0.86, 0.75)
        leg.SetTextFont(42)
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        leg.SetTextSize(0.04)
        leg.SetTextAlign(32)
        leg.AddEntry(h_OS, "OS", "lep")
        leg.AddEntry(h_SS, "SS", "lep")
        leg.Draw("SAME")

        c.SaveAs(f"plots/test/hist_OS_SS_noIDnoTrig_{ptbin_name}_{i}.pdf")


# OS-SS lephad
# ------------

def SS_1p_3p(ptbin_name, ptbin_lh, ptbin_hh):

    SS_1p = "n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 60000. && OS && is_fake" + ptbin_lh
    SS_3p = "n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 60000. && !OS && is_fake" + ptbin_lh
    path = "../ttt-ntuple-v3/ttt-lh.root"

    df_SS_1p = R.RDataFrame("Nominal", path).Filter(SS_1p)
    df_SS_1p = df_SS_1p.Define("weight_new", "weight / tauSF")

    df_SS_3p = R.RDataFrame("Nominal", path).Filter(SS_3p)
    df_SS_3p = df_SS_3p.Define("weight_new", "weight / tauSF")

    for i, pairs in enumerate([("lep_origin", "lep_origin"), ("tau_origin", "tau_origin")]):
        c = R.TCanvas(f"c", "", 900, 900)
        h_SS_1p = df_SS_1p.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[0], "weight_new").GetValue()
        h_SS_3p = df_SS_3p.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), pairs[1], "weight_new").GetValue()

        h_SS_1p.SetLineColor(R.kRed)
        h_SS_1p.SetMarkerColor(R.kRed)
        h_SS_3p.SetLineColor(R.kBlue)
        h_SS_3p.SetMarkerColor(R.kBlue)

        h_SS_1p.Scale(1.0 / h_SS_1p.Integral())
        h_SS_3p.Scale(1.0 / h_SS_3p.Integral())

        tr = R.TRatioPlot(h_SS_1p, h_SS_3p)
        tr.SetH1DrawOpt("HIST E1 SAME")
        tr.SetH2DrawOpt("HIST E1 SAME")
        tr.Draw()
        
        tr.GetUpperRefYaxis().SetRangeUser(0.0, 1.0)
        tr.GetLowerRefYaxis().SetRangeUser(0.0, 2.0)
        tr.GetLowYaxis().SetNdivisions(505)

        # ?
        tr.GetXaxis().SetBinLabel(1, "Others")
        tr.GetXaxis().SetBinLabel(2, "top->W")
        tr.GetXaxis().SetBinLabel(3, "top->b")

        text = R.TLatex()
        text.SetNDC()
        text.SetTextFont(72)
        text.SetTextSize(0.045)
        text.SetTextFont(42)
        text.SetTextSize(0.040)
        text.DrawLatex(0.46, 0.95, f"OS_SS, p_T bin: {ptbin_name}, Obj: {i}")
        
        leg = R.TLegend(0.66, 0.60, 0.86, 0.75)
        leg.SetTextFont(42)
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        leg.SetTextSize(0.04)
        leg.SetTextAlign(32)
        leg.AddEntry(h_SS_1p, "SS 1p", "lep")
        leg.AddEntry(h_SS_3p, "SS 3p", "lep")
        leg.Draw("SAME")

        c.SaveAs(f"plots/test/hist_SS_1p3p_noIDnoTrig_{ptbin_name}_{i}.pdf")


for name, bins in ptbins.items():
    bin_lh, bin_hh = bins
    # TT(name, bin_lh, bin_hh)
    # TF(name, bin_lh, bin_hh)
    # FT(name, bin_lh, bin_hh)
    # FF(name, bin_lh, bin_hh)
    # OS_SS(name, bin_lh, bin_lh)
    SS_1p_3p(name, bin_lh, bin_lh)
