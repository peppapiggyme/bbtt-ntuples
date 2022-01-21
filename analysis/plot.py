import ROOT as R
# TODO: inheritence

class TTbarInclPlot(object):
    """
    return data, ttbar and others
    """

    def __init__(self, ana, varnm, wtnm, th1bin, rebin=None):
        super().__init__()
        self._ana = ana
        self._histos = {}
        self._variableName = varnm
        self._weightName = wtnm
        self._th1binning = th1bin
        self._rebinning = rebin
        self._init_histos()
        self.data = self._merge_histos("data")
        self.ttbar = self._merge_histos("ttbar")
        self.others = self._merge_histos("others")
        self._rebin()

    def _merge_histos(self, label):
        h = None
        for i, p in enumerate(self._ana.samples[label]):
            t = self._histos[p].GetValue()
            if i == 0:
                h = t.Clone()
            else:
                h.Add(t)
        h.SetNameTitle(label, label)
        return h

    def _init_histos(self):
        for p in self._ana.processes:
            self._histos[p] = self._ana.current_df()[p].Histo1D(R.RDF.TH1DModel(
                p, self._variableName, *self._th1binning), self._variableName, self._weightName)

    def _rebin(self):
        if self._rebinning:
            self.data = self.data.Rebin(
                len(self._rebinning) - 1, "data_rebin", self._rebinning)
            self.ttbar = self.ttbar.Rebin(
                len(self._rebinning) - 1, "ttbar_rebin", self._rebinning)
            self.others = self.others.Rebin(
                len(self._rebinning) - 1, "others_rebin", self._rebinning)

    def checkYields(self):
        print(f"---------+----------------------------------")
        print(f" n_data  |   {self.data.Integral()}")
        print(f" n_ttbar |   {self.ttbar.Integral()}")
        print(f" n_other |   {self.others.Integral()}")
        print(f"---------+----------------------------------")

    def checkEntries(self):
        print(f"---------+----------------------------------")
        print(f" n_data  |   {self.data.GetEntries()}")
        print(f" n_ttbar |   {self.ttbar.GetEntries()}")
        print(f" n_other |   {self.others.GetEntries()}")
        print(f"---------+----------------------------------")

    def ana(self):
        return self._ana

    def bkgColors(self):
        return zip([self.others, self.ttbar], [(153, 204, 255), (255, 204, 102)])


class TTbarTrueFakePlot(object):
    """
    return data, ttbarTrue, ttbarFake and others
    """

    def __init__(self, ana, varnm, wtnm, th1bin, rebin=None):
        super().__init__()
        self._ana = ana
        self._histos = {}
        self._variableName = varnm
        self._weightName = wtnm
        self._th1binning = th1bin
        self._rebinning = rebin
        self._init_histos()
        self.data = self._merge_histos("data")
        self.ttbarTrue = self._merge_histos("ttbarTrue")
        self.ttbarFake = self._merge_histos("ttbarFake")
        self.stop = self._merge_histos("stop")
        self.Wjets = self._merge_histos("Wjets")
        self.others = self._merge_histos("others")
        self._rebin()

    def _merge_histos(self, label):
        h = None
        for i, p in enumerate(self._ana.samples[label]):
            t = self._histos[p].GetValue()
            if i == 0:
                h = t.Clone()
            else:
                h.Add(t)
        h.SetNameTitle(label, label)
        return h

    def _init_histos(self):
        for p in self._ana.processes:
            self._histos[p] = self._ana.current_df()[p].Histo1D(R.RDF.TH1DModel(
                p, self._variableName, *self._th1binning), self._variableName, self._weightName)

    def _rebin(self):
        if self._rebinning:
            self.data = self.data.Rebin(
                len(self._rebinning) - 1, "data_rebin", self._rebinning)
            self.ttbarTrue = self.ttbarTrue.Rebin(
                len(self._rebinning) - 1, "ttbarTrue_rebin", self._rebinning)
            self.ttbarFake = self.ttbarFake.Rebin(
                len(self._rebinning) - 1, "ttbarFake_rebin", self._rebinning)
            self.stop = self.stop.Rebin(
                len(self._rebinning) - 1, "stop_rebin", self._rebinning)
            self.Wjets = self.Wjets.Rebin(
                len(self._rebinning) - 1, "Wjets_rebin", self._rebinning)
            self.others = self.others.Rebin(
                len(self._rebinning) - 1, "others_rebin", self._rebinning)

    def checkYields(self):
        total = self.ttbarTrue.Integral() \
              + self.ttbarFake.Integral() \
              + self.others.Integral()
        print("==== Total ====")
        print(f"-------------+----------------------------------")
        print(f" n_data      |   {self.data.Integral()}")
        print(f" n_ttbarTrue |   {self.ttbarTrue.Integral()} \t({self.ttbarTrue.Integral()/total})")
        print(f" n_ttbarFake |   {self.ttbarFake.Integral()} \t({self.ttbarFake.Integral()/total})")
        print(f" n_stop      |   {self.stop.Integral()} \t({self.stop.Integral()/total})")
        print(f" n_Wjets     |   {self.Wjets.Integral()} \t({self.Wjets.Integral()/total})")
        print(f" n_others    |   {self.others.Integral()} \t({self.others.Integral()/total})")
        print(f"-------------+----------------------------------")
        
        for i in range(1, self.data.GetNbinsX()+1):
            print(f"==== Bin {i} ====")
            total = self.ttbarTrue.GetBinContent(i) \
                  + self.ttbarFake.GetBinContent(i) \
                  + self.others.GetBinContent(i)
            print(f"-------------+----------------------------------")
            print(f" n_data      |   {self.data.GetBinContent(i)}")
            print(f" n_ttbarTrue |   {self.ttbarTrue.GetBinContent(i)} +- {self.ttbarTrue.GetBinError(i)} \t({self.ttbarTrue.GetBinContent(i)/total})")
            print(f" n_ttbarFake |   {self.ttbarFake.GetBinContent(i)} +- {self.ttbarFake.GetBinError(i)} \t({self.ttbarFake.GetBinContent(i)/total})")
            print(f" n_stop      |   {self.stop.GetBinContent(i)} +- {self.stop.GetBinError(i)} \t({self.stop.GetBinContent(i)/total})")
            print(f" n_Wjets     |   {self.Wjets.GetBinContent(i)} +- {self.Wjets.GetBinError(i)} \t({self.Wjets.GetBinContent(i)/total})")
            print(f" n_other     |   {self.others.GetBinContent(i)} +- {self.others.GetBinError(i)} \t({self.others.GetBinContent(i)/total})")
            print(f"-------------+----------------------------------")

    def checkEntries(self):
        print(f"---------+----------------------------------")
        print(f" n_data      |   {self.data.GetEntries()}")
        print(f" n_ttbarTrue |   {self.ttbarTrue.GetEntries()}")
        print(f" n_ttbarFake |   {self.ttbarFake.GetEntries()}")
        print(f" n_stop      |   {self.stop.GetEntries()}")
        print(f" n_Wjets     |   {self.Wjets.GetEntries()}")
        print(f" n_other     |   {self.others.GetEntries()}")
        print(f"---------+----------------------------------")

    def checkTTBarNorm(self):
        """
        Use this only when filling 1 bin!
        """
        if self._th1binning[0] != 1 or (self._rebinning and len(self._rebinning) != 2):
            print("Warning: please fill one bin otherwise no garentee of precision!")
        norm  = (self.data.Integral() - self.stop.Integral() - self.Wjets.Integral() - self.others.Integral()) / (self.ttbarTrue.Integral() + self.ttbarFake.Integral())
        st_up = (self.data.Integral() - 1.2 * self.stop.Integral() - self.Wjets.Integral() - self.others.Integral()) / (self.ttbarTrue.Integral() + self.ttbarFake.Integral())
        st_dn = (self.data.Integral() - 0.8 * self.stop.Integral() - self.Wjets.Integral() - self.others.Integral()) / (self.ttbarTrue.Integral() + self.ttbarFake.Integral())
        wj_up = (self.data.Integral() - self.stop.Integral() - 1.4 * self.Wjets.Integral() - 1.4 * self.others.Integral()) / (self.ttbarTrue.Integral() + self.ttbarFake.Integral())
        wj_dn = (self.data.Integral() - self.stop.Integral() - 0.6 * self.Wjets.Integral() - 0.6 * self.others.Integral()) / (self.ttbarTrue.Integral() + self.ttbarFake.Integral())
        print(f"> the nominal ttbar norm  is {norm}")
        print(f"> the nominal ttbar st_up is {st_up} [{(st_up - norm) / norm * 100}%]")
        print(f"> the nominal ttbar st_dn is {st_dn} [{(st_dn - norm) / norm * 100}%]")
        print(f"> the nominal ttbar wj_up is {wj_up} [{(wj_up - norm) / norm * 100}%]")
        print(f"> the nominal ttbar wj_dn is {wj_dn} [{(wj_dn - norm) / norm * 100}%]")

        return norm

    def ana(self):
        return self._ana

    def bkgColors(self):
        # return zip([self.others, self.ttbarFake, self.ttbarTrue], [(153, 204, 255), (255, 153, 153), (255, 255, 153)])
        return zip([self.others, self.Wjets, self.stop, self.ttbarFake, self.ttbarTrue], 
                   [(34, 140, 121), (137, 90, 145), (224, 151, 94), (245, 184, 37), (247, 245, 111)])


class TTbarSystPlotCollection(object):
    """
    return data, ttbar and others
    """

    def __init__(self, ana, varnm, wt_prefix, wt_suffix, systs, th1bin, rebin=None):
        super().__init__()

        self._systematics = systs
        self._nomPlot = TTbarTrueFakePlot(ana, varnm, wt_prefix + "Nominal" + wt_suffix, th1bin, rebin)
        self._systPlots = {}
        for syst in self._systematics:
            self._systPlots[syst] = (
                TTbarTrueFakePlot(ana, varnm, wt_prefix + syst + "__1up" + wt_suffix, th1bin, rebin), 
                TTbarTrueFakePlot(ana, varnm, wt_prefix + syst + "__1down" + wt_suffix, th1bin, rebin)
            )
            
    def nominalPlot(self):
        return self._nomPlot
    
    def systematicPlots(self):
        return self._systPlots
    
    def numberOfSysts(self):
        assert(len(self._systPlots) == len(self._systematics))
        return len(self._systPlots)

    def checkYields(self):
        print("Nominal:")
        print(f"-------------+----------------------------------")
        print(f" n_data      |   {self._nomPlot.data.Integral()}")
        print(f" n_ttbarTrue |   {self._nomPlot.ttbarTrue.Integral()}")
        print(f" n_ttbarFake |   {self._nomPlot.ttbarFake.Integral()}")
        print(f" n_other     |   {self._nomPlot.others.Integral()}")
        print(f"-------------+----------------------------------")
        for syst in self._systematics:
            print(f"{syst}__1up:")
            print(f"-------------+----------------------------------")
            print(f" n_data      |   {self._systPlots[syst][0].data.Integral()}")
            print(f" n_ttbarTrue |   {self._systPlots[syst][0].ttbarTrue.Integral()}")
            print(f" n_ttbarFake |   {self._systPlots[syst][0].ttbarFake.Integral()}")
            print(f" n_other     |   {self._systPlots[syst][0].others.Integral()}")
            print(f"-------------+----------------------------------")
            print(f"{syst}__1down:")
            print(f"-------------+----------------------------------")
            print(f" n_data      |   {self._systPlots[syst][1].data.Integral()}")
            print(f" n_ttbarTrue |   {self._systPlots[syst][1].ttbarTrue.Integral()}")
            print(f" n_ttbarFake |   {self._systPlots[syst][1].ttbarFake.Integral()}")
            print(f" n_other     |   {self._systPlots[syst][1].others.Integral()}")
            print(f"-------------+----------------------------------")
