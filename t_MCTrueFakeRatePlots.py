import ROOT as R
R.gROOT.SetBatch(True)
R.gROOT.SetStyle("ATLAS")
R.gStyle.SetErrorX(0.5)
R.gInterpreter.ProcessLine("ROOT::EnableImplicitMT();")


truth_types = ["G", "D", "U", "S", "C", "B", "O", "A"]
prongs = ["1P", "3P"]
triggers = ["None", "25", "35", "25EF", "35EF", "25RNN", "35RNN"]

f_lh = R.TFile("rootfiles/MCTrueFakeLepHad.root")
f_lh.ls()
f_hh = R.TFile("rootfiles/MCTrueFakeHadHad.root")

for truth_type in truth_types:
    for prong in prongs:
        for trigger in triggers:
            name = f"fakerate_mc_{truth_type}_trig{trigger}_{prong}"
            
            eff_lh = f_lh.Get(name).CreateGraph().Clone("lephad")
            eff_hh = f_hh.Get(name).CreateGraph().Clone("hadhad")
            
            mg = R.TMultiGraph()
            eff_lh.SetLineColor(R.kRed)
            eff_lh.SetMarkerColor(R.kRed)
            # eff_lh.SetMaximum(max(eff_lh.GetMaximum(), eff_hh.GetMaximum()) * 1.4)
            eff_hh.SetLineColor(R.kBlue)
            eff_hh.SetMarkerColor(R.kBlue)

            c = R.TCanvas(f"c_{name}", "", 800, 600)
            c.SetLogx()
            mg.Add(eff_lh, "AP")
            mg.Add(eff_hh, "AP")
            mg.Draw("ACP")
            
            c.SaveAs(f"plots/test/c_{name}.png")
