from ROOT import gStyle, gROOT
from ROOT import TFile, TEfficiency, TCanvas, TGraphAsymmErrors, TMultiGraph, TLegend, TLatex
from ROOT import kRed, kBlue, kMagenta
from collections import OrderedDict
from array import array
gROOT.SetBatch(True)
gStyle.SetEndErrorSize(5)
gROOT.SetStyle("ATLAS")
gStyle.SetErrorX(0.5)

f = TFile("rootfiles/ttbar-fakerates.root")
# f.ls()
dNom = f.Get("Nominal")
# dNom.ls()
dStatU = f.Get("TTBarReweight_Stat__1up")
dStatD = f.Get("TTBarReweight_Stat__1down")

dSysts = OrderedDict()
dSysts = {
    "ttbarReweightStat" : [dStatU, dStatD],
}

trigs = ["00", "25", "35", "25EF", "35EF", "25RNN", "35RNN"]
prongs = ["1P", "3P"]

mc = [(21, kRed+1), (22, kBlue+1), (23, kMagenta+1)]

for trig in trigs:
    for prong in prongs:
        fileName = f"plots/fakerate/fakerate_data_trig{trig}_{prong}.pdf"
        mg = TMultiGraph()
        mg.SetName("Fake Rates")
        c = TCanvas(f"c_{trig}_{prong}", "", 900, 900)
        c.SetLogx()

        leg = TLegend(0.50, 0.55, 0.90, 0.75)
        leg.SetTextFont(42)
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        leg.SetTextSize(0.036)
        leg.SetTextAlign(32)

        gNom = dNom.Get(f"fakerate_data_trig{trig}_{prong}").CreateGraph()
        x = gNom.GetX()
        y = gNom.GetY()
        x = array('d', [i / 1000 for i in x])
        exH = array('d', [gNom.GetErrorXhigh(i) / 1000 for i in range(len(x))])
        exL = array('d', [gNom.GetErrorXlow(i)  / 1000 for i in range(len(x))])
        eWidth = array('d', [h + l for h, l in zip(exH, exL)])
        x = array('d', [x[i] - 0.4 * eWidth[i] for i in range(len(x))])
        exH = array('d', [e + 0.4 * eWidth[i] for i, e in enumerate(exH)])
        exL = array('d', [e - 0.4 * eWidth[i] for i, e in enumerate(exL)])
        gNomGeV = TGraphAsymmErrors(len(x), x, y, exL, exH, gNom.GetEYlow(), gNom.GetEYhigh())
        leg.AddEntry(gNomGeV, "Nominal", "lep")
        for j, (nm, ud) in enumerate(dSysts.items()):
            dU, dD = ud
            gU = dU.Get(f"fakerate_data_trig{trig}_{prong}").CreateGraph()
            gD = dD.Get(f"fakerate_data_trig{trig}_{prong}").CreateGraph()
            yU = gU.GetY()
            yD = gD.GetY()
            xHere = array('d', [x[i] + 0.2 * (j + 1) * eWidth[i] for i in range(len(x))])
            eU = array('d', [u - n for u, n in zip(yU, y)])
            eD = array('d', [d - n for d, n in zip(yD, y)])
            eH = array('d', [e - 0.2 * (j + 1) * eWidth[i] for i, e in enumerate(exH)])
            eL = array('d', [e + 0.2 * (j + 1) * eWidth[i] for i, e in enumerate(exL)])
            # for display ...
            for i in range(len(eU)):
                if eU[i] < eD[i]: # eU < 0
                    eU[i], eD[i] = eD[i], eU[i]
            gSyst = TGraphAsymmErrors(len(x), xHere, y, eL, eH, eU, eU)
            gSyst.SetName(nm)
            gSyst.SetMarkerStyle(mc[j][0])
            gSyst.SetMarkerColor(mc[j][1])
            gSyst.SetLineColor(mc[j][1])
            leg.AddEntry(gSyst, nm, "lep")
            mg.Add(gSyst, "p")

        mg.Add(gNomGeV, "p")
        mg.Draw("ap")
        mg.GetXaxis().SetTitle("#tau p_{T} [GeV]")
        mg.SetMinimum(0.)

        text = TLatex()
        text.SetNDC()
        text.SetTextFont(72)
        text.SetTextSize(0.045)
        # text.DrawLatex(0.51, 0.86, "ATLAS")
        # text.SetTextFont(42)
        # text.DrawLatex(0.51 + 0.16, 0.86, "Internal")
        # text.SetTextSize(0.040)
        # text.DrawLatex(0.51, 0.80, "#sqrt{s} = 13 TeV, 139 fb^{-1}")
        text.SetTextFont(42)
        text.SetTextSize(0.040)
        text.DrawLatex(0.46, 0.86, f"trigger: {trig}, prong: {prong}")

        leg.Draw("SAME")

        c.SaveAs(fileName)

for trig in trigs:
    for prong in prongs:
        fileName = f"plots/fakerate/fakerate_vsmc_trig{trig}_{prong}.pdf"
        mg = TMultiGraph()
        mg.SetName("Fake Rates")
        c = TCanvas(f"c_data_vs_mc_{trig}_{prong}", "", 900, 900)
        c.SetLogx()
        gData = dNom.Get(f"fakerate_data_trig{trig}_{prong}").CreateGraph()
        x = gData.GetX()
        y = gData.GetY()
        x = array('d', [i / 1000 for i in x])
        exH = array('d', [gData.GetErrorXhigh(i) / 1000 for i in range(len(x))])
        exL = array('d', [gData.GetErrorXlow(i)  / 1000 for i in range(len(x))])
        eWidth = array('d', [h + l for h, l in zip(exH, exL)])
        gDataGeV = TGraphAsymmErrors(len(x), x, y, exL, exH, gData.GetEYlow(), gData.GetEYhigh())
        mg.Add(gDataGeV, "p")

        gMC = dNom.Get(f"fakerate_mc_trig{trig}_{prong}").CreateGraph()
        x = gMC.GetX()
        y = gMC.GetY()
        x = array('d', [i / 1000 for i in x])
        exH = array('d', [gMC.GetErrorXhigh(i) / 1000 for i in range(len(x))])
        exL = array('d', [gMC.GetErrorXlow(i)  / 1000 for i in range(len(x))])
        eWidth = array('d', [h + l for h, l in zip(exH, exL)])
        gMCGeV = TGraphAsymmErrors(len(x), x, y, exL, exH, gMC.GetEYlow(), gMC.GetEYhigh())
        gMCGeV.SetMarkerStyle(mc[0][0])
        gMCGeV.SetMarkerColor(mc[0][1])
        gMCGeV.SetLineColor(mc[0][1])
        mg.Add(gMCGeV, "p")
        mg.Draw("ap")
        mg.GetXaxis().SetTitle("#tau p_{T} [GeV]")
        mg.SetMinimum(0.)

        leg = TLegend(0.60, 0.55, 0.80, 0.75)
        leg.SetTextFont(42)
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        leg.SetTextSize(0.04)
        leg.SetTextAlign(32)
        leg.AddEntry(gDataGeV, "Data FR", "lep")
        leg.AddEntry(gMCGeV, "MC FR", "lep")
        leg.Draw("SAME")

        text = TLatex()
        text.SetNDC()
        text.SetTextFont(72)
        text.SetTextSize(0.045)
        # text.DrawLatex(0.51, 0.86, "ATLAS")
        # text.SetTextFont(42)
        # text.DrawLatex(0.51 + 0.16, 0.86, "Internal")
        # text.SetTextSize(0.040)
        # text.DrawLatex(0.51, 0.80, "#sqrt{s} = 13 TeV, 139 fb^{-1}")
        text.SetTextFont(42)
        text.SetTextSize(0.040)
        text.DrawLatex(0.46, 0.86, f"trigger: {trig}, prong: {prong}")

        c.SaveAs(fileName)


f.Close()
