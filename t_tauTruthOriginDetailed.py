import ROOT as R
R.gROOT.SetBatch(True)
R.gROOT.SetStyle("ATLAS")
R.gStyle.SetErrorX(0.5)


for i in range(3, 9):
    region = f"n_btag == 2 && n_jets >= 2 && ((mBB > 150000. && mBB < 350000.) || (mBB > 50000. && mBB < 100000.)) && mTW > 60000. && OS && is_fake && tau_truth == {i}"
    path = "../ttt-ntuple-v4/ttt-lh.root"
    df_lephad = R.RDataFrame("Nominal", path).Filter(region)
    df_lephad = df_lephad.Define("weight_new", "weight / tauSF")

    c = R.TCanvas(f"c", "", 900, 900)
    h_lephad = df_lephad.Histo1D(R.RDF.TH1DModel("ttbar", "#tau_{had} truth origin", 3, 0, 3), "tau_origin", "weight_new").GetValue()

    h_lephad.Draw("HIST")

    c.SaveAs(f"hist_fakeTTBar_noIDnoTrig_tauTruth_{i}.pdf")
