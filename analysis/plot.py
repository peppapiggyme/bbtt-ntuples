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
                len(self._rebinning) - 1, "others_rebin", self._rebinning)
            self.others = self.others.Rebin(
                len(self._rebinning) - 1, "others_rebin", self._rebinning)

    def checkYields(self):
        print(f"-------------+----------------------------------")
        print(f" n_data      |   {self.data.Integral()}")
        print(f" n_ttbarTrue |   {self.ttbarTrue.Integral()}")
        print(f" n_ttbarFake |   {self.ttbarFake.Integral()}")
        print(f" n_other     |   {self.others.Integral()}")
        print(f"-------------+----------------------------------")

    def ana(self):
        return self._ana

    def bkgColors(self):
        return zip([self.others, self.stop, self.ttbarFake, self.ttbarTrue], [(153, 204, 255), (46, 97, 80), (255, 153, 153), (255, 255, 153)])


class TTbarSystPlotCollection(object):
    """
    return data, ttbar and others
    """

    def __init__(self, ana, varnm, wt_suffix, systs, th1bin, rebin=None):
        super().__init__()

        self._systematics = systs
        self._nomPlot = TTbarTrueFakePlot(ana, varnm, "Nominal" + wt_suffix, th1bin, rebin)
        self._systPlots = {}
        for syst in self._systematics:
            self._systPlots[syst] = (
                TTbarTrueFakePlot(ana, varnm, syst + "__1up" + wt_suffix, th1bin, rebin), 
                TTbarTrueFakePlot(ana, varnm, syst + "__1down" + wt_suffix, th1bin, rebin)
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
