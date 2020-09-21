import ROOT as R
R.gROOT.SetBatch(True)
R.gROOT.SetStyle("ATLAS")
R.gStyle.SetErrorX(0.5)
import random
import array


class HistPlot(object):
    def __init__(self, x, name, title, xtitle, ytitle, xbins):
        super().__init__()
        self.xVar = x
        self.name = name
        self.title = title
        self.xTitle = xtitle
        self.yTitle = ytitle
        self.binning = xbins

class ProfilePlot(object):
    def __init__(self, x, y, name, title, xtitle, ytitle, xbins, rebin=None):
        super().__init__()
        self.xVar = x
        self.yVar = y
        self.name = name
        self.title = title
        self.xTitle = xtitle
        self.yTitle = ytitle
        self.binning = xbins
        self.rebin = rebin

def drawHistogram(plot):
    c = R.TCanvas(f"c", "", 900, 900)

    region = "n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 60000. && OS && (lep_origin != 1 || tau_origin != 1)"
    path = "../ttt-ntuple-v4/ttt-lh.root"

    df_lephad = R.RDataFrame("Nominal", path).Filter(region)
    df_lephad = df_lephad.Define("weight_new", "weight / tauSF")

    g = df_lephad.Histo1D(R.RDF.TH1DModel(plot.name, plot.title, *(plot.binning)), plot.xVar, "weight_new").GetValue()
    g.SetLineColor(R.kBlue)
    g.GetXaxis().SetTitle(plot.xTitle)
    g.GetYaxis().SetTitle(plot.yTitle)
    g.Draw()
    c.SaveAs(f"histogram_{plot.name}.pdf")

def drawProfile(plot, truth):
    """
    truth = WW WO OW OO
    """
    c = R.TCanvas(f"c", "", 900, 900)

    path = "../ttt-ntuple-v4/ttt-lh.root"

    baseCut = "n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 60000. && OS"

    truthCut = None
    WW = baseCut + " && (lep_origin == 1 && tau_origin == 1)"
    WO = baseCut + " && (lep_origin == 1 && tau_origin != 1)"
    OW = baseCut + " && (lep_origin != 1 && tau_origin == 1)"
    OO = baseCut + " && (lep_origin != 1 && tau_origin != 1)"

    if truth == "WW":
        truthCut = baseCut + " && (lep_origin == 1 && tau_origin == 1)"
    elif truth == "WO":
        truthCut = baseCut + " && (lep_origin == 1 && tau_origin != 1)"
    elif truth == "OW":
        truthCut = baseCut + " && (lep_origin != 1 && tau_origin == 1)"
    else: # OO
        truthCut = baseCut + " && (lep_origin != 1 && tau_origin != 1)"

    df = R.RDataFrame("Nominal", path).Filter(truthCut).Define("weight_new", "weight / tauSF")
    col = R.kBlack

    g = df.Profile1D(R.RDF.TProfile1DModel(plot.name, plot.title, *(plot.binning), "s"), plot.xVar, plot.yVar, "weight_new").GetValue()
    R.TProfile.Approximate(True)
    g.BuildOptions(50000., 2000000., 's')
    # g.Draw()
    if not plot.rebin:
        h = g.ProjectionX()
    else:
        h = g.Rebin(len(plot.rebin) - 1, plot.name + "_rebin", plot.rebin)
    h.SetLineColor(col)
    h.SetMarkerColor(col)
    h.SetMarkerSize(0)
    h.GetXaxis().SetTitle(plot.xTitle)
    h.GetYaxis().SetTitle(plot.yTitle)
    h.SetMaximum(plot.binning[2])
    h.SetMinimum(plot.binning[1])
    h.SetName(f"fTrans_{plot.name}_{truth}")
    h.Draw("HIST E1 SAME")
    # expr = "[0]+[1]*x"
    # f = R.TF1(f"myfunc", expr, h.GetXaxis().GetXmin(),
    #         h.GetXaxis().GetXmax(), 2)
    # h.Fit(f)
    # f.SetLineColor(col - 2 if col != R.kBlack else R.kGray)
    # f.Draw("SAME")

    c.SaveAs(f"graph_kl_{plot.name}_{truth}.png")


def drawProfileAll(plot):
    """
    w = f_l ( x^Reco_l )
      = f_l ( k_l ( x^Truth_l ) )
      = g_l ( x^Truth_l )
      =universal= g ( x^Truth )

    where k_l and g depends on truth origin (WW, WO, OW, OO)
    in other region, must always use f_l and k_l

    -> g = f_l o k_l
    """
    c = R.TCanvas(f"c", "", 900, 900)

    fOut = R.TFile(f"./rootfiles/ttbar-truth-{plot.name}.root", "recreate")
    path = "../ttt-ntuple-v4/ttt-lh.root"

    baseCut = "n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 60000. && OS"

    WW = baseCut + " && (lep_origin == 1 && tau_origin == 1)"
    WO = baseCut + " && (lep_origin == 1 && tau_origin != 1)"
    OW = baseCut + " && (lep_origin != 1 && tau_origin == 1)"
    OO = baseCut + " && (lep_origin != 1 && tau_origin != 1)"

    df_WW = R.RDataFrame("Nominal", path).Filter(WW)
    df_WO = R.RDataFrame("Nominal", path).Filter(WO)
    df_OW = R.RDataFrame("Nominal", path).Filter(OW)
    df_OO = R.RDataFrame("Nominal", path).Filter(OO)
    
    df_WW = df_WW.Define("weight_new", "weight / tauSF")
    df_WO = df_WO.Define("weight_new", "weight / tauSF")
    df_OW = df_OW.Define("weight_new", "weight / tauSF")
    df_OO = df_OO.Define("weight_new", "weight / tauSF")

    for df, col, name in [(df_WW, R.kBlack, "WW"), 
                          (df_WO, R.kBlue, "WO"), 
                          (df_OW, R.kMagenta, "OW"), 
                          (df_OO, R.kRed, "OO")]:
        g = df.Profile1D(R.RDF.TProfile1DModel(plot.name, plot.title, *(plot.binning), "s"), plot.xVar, plot.yVar, "weight_new").GetValue()
        R.TProfile.Approximate(True)
        g.BuildOptions(50000., 2000000., 's')
        # g.Draw()
        if not plot.rebin:
            h = g.ProjectionX()
        else:
            h = g.Rebin(len(plot.rebin) - 1, plot.name + "_rebin", plot.rebin)
            h = h.ProjectionX()
        h.SetLineColor(col)
        h.SetMarkerColor(col)
        h.SetMarkerSize(0)
        h.GetXaxis().SetTitle(plot.xTitle)
        h.GetYaxis().SetTitle(plot.yTitle)
        h.SetMaximum(plot.binning[2])
        h.SetMinimum(plot.binning[1])
        h.SetName(f"fTrans_{plot.name}_{name}")
        h.Draw("HIST E1 SAME")
        fOut.cd()
        print(type(h))
        h.Write()
        # expr = "[0]+[1]*x"
        # f = R.TF1(f"myfunc", expr, h.GetXaxis().GetXmin(),
        #         h.GetXaxis().GetXmax(), 2)
        # h.Fit(f)
        # f.SetLineColor(col - 2 if col != R.kBlack else R.kGray)
        # f.Draw("SAME")

    c.SaveAs(f"graph_kl_{plot.name}.png")
    fOut.Close()

# don't need n_jets
# p = ProfilePlot("nTruthJets20", "n_jets", "njets", "# jets", "true # jets", "reco # jets", (13, 0, 13))
# drawProfile(p)

# p = ProfilePlot("dRbb_truth", "dRbb", "dRbb", "#DeltaR(b, b)", "true #DeltaR(b, b)", "reco #DeltaR(b, b)", (120, 0, 6))
# drawProfile(p)

# dRbb might not be necessary, either
# p = HistPlot("dRbb", "dRbb", "#DeltaR(b, b)", "reco #DeltaR(b, b)", "Event", (120, 0, 6))
# drawHistogram(p)

# p = HistPlot("dRbb_truth", "dRbb_truth", "#DeltaR(b, b)", "reco #DeltaR(b, b)", "Event", (120, 0, 6))
# drawHistogram(p)


# HT
binAll = [0, 100000]
bin0 = [i for i in range(120000, 200000, 10000)]
bin1 = [i for i in range(200000, 600000, 10000)]
bin2 = [i for i in range(600000, 800000, 20000)]
bin3 = [800000, 825000, 850000, 875000, 900000, 950000, 1000000, 1200000, 1400000, 2000000]
binAll.extend(bin0)
binAll.extend(bin1)
binAll.extend(bin2)
binAll.extend(bin3)
p = ProfilePlot("ST_truth", "ST", "sum_pt", "Sum of p_T", "true Sum of lep, tau, b, b pT", "reco Sum of lep, tau, jets", (200, 0, 2000000), rebin=array.array('d', binAll))
drawProfile(p, "WW")
drawProfile(p, "WO")
drawProfile(p, "OW")
drawProfile(p, "OO")
drawProfileAll(p)

# dRll
binAll = [0.0, 0.4]
bin0 = [float(i*0.1) for i in range(5, 50, 1)]
bin1 = [5.0, 5.25, 6.0] # anyway the dRlh are in one bin for the reweighting
binAll.extend(bin0)
binAll.extend(bin1)

p = ProfilePlot("dRll_truth", "dRTauLep", "dRll", "#DeltaR(lep, tau)", "true #DeltaR(lep, tau)", "reco #DeltaR(lep, tau)", (120, 0, 6), rebin=array.array('d', binAll))
drawProfile(p, "WW")
drawProfile(p, "WO")
drawProfile(p, "OW")
drawProfile(p, "OO")
drawProfileAll(p)
