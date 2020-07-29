import ROOT as R
import os

# lambda helper


def rootfile(x): return x + ".root"


# regions definition
reg = {}
reg["NoID"] = "n_btag == 2 && n_jets >= 2 && mBB > 150000. && mTW > 50000."
reg["NoID OS"] = reg["NoID"] + " && OS"
reg["NoID SS"] = reg["NoID"] + " && !OS"
reg["NoID OS 1P"] = reg["NoID OS"] + " && tau_prong == 1"
reg["NoID OS 3P"] = reg["NoID OS"] + " && tau_prong == 3"
reg["NoID SS 1P"] = reg["NoID SS"] + " && tau_prong == 1"
reg["NoID SS 3P"] = reg["NoID SS"] + " && tau_prong == 3"

reg["PassID"] = reg["NoID"] + " && tau_loose"
reg["PassID OS"] = reg["PassID"] + " && OS"
reg["PassID SS"] = reg["PassID"] + " && !OS"
reg["PassID OS 1P"] = reg["PassID OS"] + " && tau_prong == 1"
reg["PassID OS 3P"] = reg["PassID OS"] + " && tau_prong == 3"
reg["PassID SS 1P"] = reg["PassID SS"] + " && tau_prong == 1"
reg["PassID SS 3P"] = reg["PassID SS"] + " && tau_prong == 3"


class AnaBase(object):
    def __init__(self, tauid, isOS=None, prong=None):
        self._tauid = tauid
        self._isOS = isOS
        self._prong = prong

        self._region = "PassID" if tauid else "NoID"
        if isOS:
            self._region += " " + "OS" if isOS else "SS"
        if prong:
            self._region += " " + "1P" if prong == 1 else "3P"

        print(f"analysis region is [{self._region}]")
        print(f"selection is [{reg[self._region]}]")

        self.path = "/Users/bowen/Documents/work/Resolved/NtupleAna/fr-ntuple-v2/"
        self.samples = {}
        self.processes = set()
        self.files = {}
        self.df = {}  # -> the df without filter applied
        self._current_df = {}  # -> the df with filter applied

    def set_current_df(self, new_df):
        self._current_df = new_df

    def current_df(self):
        return self._current_df

    def applyWeight(self, rwt1d=None):
        """
        rwt1d is (varName, header_path)
        """
        if rwt1d:
            rtf = R.TFile("/Users/bowen/Documents/work/Resolved/NtupleAna/RDFAnalysis/rootfiles/func.root")
            R.gInterpreter.ProcessLine("auto myfunc = Rw1DFunc;")
            R.gInterpreter.Declare(f"#include \"{rwt1d[1]}\"")
            ttbarWeight = f"(float)eval_reweighter1d({rwt1d[0]})"
            if not self._tauid:
                for p in self.processes:
                    # NOTE: hardcoded name but should be safe, since process names are unique
                    if p.startswith("ttbar"):
                        self.df[p] = self.df[p].Define(
                            "weight_new", f"weight * {ttbarWeight}")
                    else:
                        self.df[p] = self.df[p].Define("weight_new", "weight")
            else:
                for p in self.processes:
                    # NOTE: hardcoded name but should be safe, since process names are unique
                    if p.startswith("ttbar"):
                        self.df[p] = self.df[p].Define(
                            "weight_new", f"weight * tauSF * {ttbarWeight}")
                    else:
                        self.df[p] = self.df[p].Define("weight_new", f"weight * tauSF")
        else:
            if not self._tauid:
                for p in self.processes:
                    self.df[p] = self.df[p].Define("weight_new", "weight")
            else:
                for p in self.processes:
                    self.df[p] = self.df[p].Define("weight_new", "weight * tauSF")


class AnaTTbarIncl(AnaBase):
    def __init__(self, tauid, isOS=None, prong=None):
        super().__init__(tauid, isOS, prong)

        self.samples = {
            "data": {"data"},
            "ttbar": {"ttbarIncl"},
            "others": {"ttH", "VHbb", "stop", "diboson", "Zee",
                       "Ztautau", "Zmumu", "Wmunu", "Wenu", "Wtaunu",
                       "Htautau"},
        }

        for label, pros in self.samples.items():
            for p in pros:
                self.processes.add(p)

        for p in self.processes:
            self.files[p] = os.path.join(self.path, rootfile(p))

        for p in self.processes:
            self.df[p] = R.RDataFrame("Nominal", self.files[p])

        for p in self.processes:
            self.df[p] = self.df[p].Filter(reg[self._region])

        self._current_df = self.df


class AnaTTbarTrueFake(AnaBase):
    def __init__(self, tauid, isOS=None, prong=None):
        super().__init__(tauid, isOS, prong)

        self.samples = {
            "data": {"data"},
            "ttbarTrue": {"ttbarTrue"},
            "ttbarFake": {"ttbarFake"},
            "others": {"ttH", "VHbb", "stop", "diboson", "Zee",
                       "Ztautau", "Zmumu", "Wmunu", "Wenu", "Wtaunu",
                       "Htautau"},
        }

        for label, pros in self.samples.items():
            for p in pros:
                self.processes.add(p)

        for p in self.processes:
            self.files[p] = os.path.join(self.path, rootfile(p))

        for p in self.processes:
            self.df[p] = R.RDataFrame("Nominal", self.files[p])

        self._current_df = self.df
