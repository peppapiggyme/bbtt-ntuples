import ROOT as R
import os

# lambda helper


def rootfile(x): return x + ".root"


# regions definition
# ------------------

# DON'T FORGET TO CHECK THE PRESELECTION FOR FR REGION !!!

reg = {}
reg["NoID"] = "n_btag == 2 && n_jets >= 2 && mBB > 150000.&& mTW > 40000." # <- !!!

def update_region():
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

update_region()

class AnaBase(object):
    def __init__(self, tauid, isOS=None, prong=None, morecut=None, rewrite=None, path=None):
        self._tauid = tauid
        self._isOS = isOS
        self._prong = prong

        self._region = "PassID" if tauid else "NoID"
        if isOS:
            self._region += " "
            self._region += "OS" if isOS else "SS"
        if prong:
            self._region += " "
            self._region += "1P" if prong == 1 else "3P"
        if morecut:
            reg["NoID"] += " && "
            reg["NoID"] += morecut
            update_region()
        if rewrite:
            reg["NoID"] = rewrite
            update_region()

        
        self.path = f"{os.getcwd()}/../fr-ntuple-v17/" if not path else path
        self.samples = {}
        self.processes = set()
        self.files = {}
        self.df = {}  # -> the df without filter applied
        self._current_df = {}  # -> the df with filter applied

        self.regionTeX = reg[self._region]
        
        print(f"> ntuple path: {self.path}")
        print(f"> analysis region is [{self._region}]")
        print(f"> selection is [{reg[self._region]}]")

    def set_current_df(self, new_df):
        self._current_df = new_df

    def current_df(self):
        return self._current_df

    def applyTauSF(self, weight_name):
        """
        TODO: seperate data from the processes. So far it's ok since tauSF and weight are 1 for data
        """
        if not self._tauid:
            for p in self.processes:
                self.df[p] = self.df[p].Define(f"{weight_name}_new", f"{weight_name} / tauSF")
        else:
             for p in self.processes:
                self.df[p] = self.df[p].Define(f"{weight_name}_new", f"{weight_name}")
    
    def applyTauSFAndFakeRate(self, weight_name):
        if not self._tauid:
            for p in self.processes:
                if p.startswith("ttbarFake"):
                    self.df[p] = self.df[p].Define(f"{weight_name}_new", f"{weight_name} / tauSF * fakeRate")
                else:
                    self.df[p] = self.df[p].Define(f"{weight_name}_new", f"{weight_name} * fakeRate")
        else:
            raise ValueError("Current only support no ID:\n"
                             " - the fake rate is apply on ttbar\n"
                             " - the fake rate for data and other MC is 0\n"
                             " - the tau scale factors are applied on the other MC\n")

    def applyTauSFAndTTBarNorm(self, old_wt="weight", new_wt="weight_new", norm_factor=0.931):
        """
        this is the baseline strategy for resonance analysis
        the corresponding ttbar reweighting region must match to the nom_factor
        e.g. nom_factor = 0.931 <-> lh SLT presel + mbb150 + mtw40 (= fake rate derive region)
        @todo: the nom_factor can be calculated within this package easily...
        """
        if not self._tauid:
            for p in self.processes:
                if p.startswith("ttbar"):
                    self.df[p] = self.df[p].Define(f"{new_wt}", f"{old_wt} * {norm_factor} / tauSF")
                else:    
                    self.df[p] = self.df[p].Define(f"{new_wt}", f"{old_wt} / tauSF")
        else:
             for p in self.processes:
                if p.startswith("ttbar"):
                    self.df[p] = self.df[p].Define(f"{new_wt}", f"{old_wt} * {norm_factor}")
                else:
                    self.df[p] = self.df[p].Define(f"{new_wt}", f"{old_wt}")

    def applyTauSFAndWeightBBLL(self, old_wt="weight", new_wt="weight_new"):
        """
        apply the bbll 1D linear function reweighting (b0_pt)
        """
        ttbarWeight = "(1.05 - 0.000001 * b0_pt)"
        if not self._tauid:
            for p in self.processes:
                if p.startswith("ttbar"):
                    self.df[p] = self.df[p].Define(
                        "weight_new", f"weight / tauSF * {ttbarWeight}")
                else:
                    self.df[p] = self.df[p].Define("weight_new", "weight / tauSF")
        else:
            for p in self.processes:
                # NOTE: hardcoded name but should be safe, since process names are unique
                if p.startswith("ttbar"):
                    self.df[p] = self.df[p].Define(
                        "weight_new", f"weight * {ttbarWeight}")
                else:
                    self.df[p] = self.df[p].Define(
                        "weight_new", f"weight")

    def applyTauSFAndTTBarNormAndWeightNjets(self, old_wt, new_wt, rwt1d=None, suffix=None, norm_factor=0.931):
        """
        rwt1d is (varName, header_path)
        apply on current df, by a given njets (indicated in the suffix)
        """
        if rwt1d:
            rtf = R.TFile(
                f"{os.getcwd()}/rootfiles/func{suffix}.root")
            R.gInterpreter.ProcessLine(f"TH1* hCorr{suffix} = (TH1*)Rw1DHist{suffix}->Clone(); hCorr{suffix}->SetDirectory(0);")
            R.gInterpreter.Declare(f"#include \"{rwt1d[1]}\"")
            ttbarWeight = f"(float)eval_reweighter{suffix}({rwt1d[0]})"
            if not self._tauid:
                for p in self.processes:
                    # NOTE: hardcoded name but should be safe, since process names are unique
                    if p.startswith("ttbar"):
                        self._current_df[p] = self._current_df[p].Define(
                            f"{new_wt}", f"{old_wt} / tauSF * {ttbarWeight} * {norm_factor}")
                    else:
                        self._current_df[p] = self._current_df[p].Define(f"{new_wt}", f"{old_wt} / tauSF")
            else:
                for p in self.processes:
                    # NOTE: hardcoded name but should be safe, since process names are unique
                    if p.startswith("ttbar"):
                        self._current_df[p] = self._current_df[p].Define(
                            f"{new_wt}", f"{old_wt} * {ttbarWeight} * {norm_factor}")
                    else:
                        self._current_df[p] = self._current_df[p].Define(
                            f"{new_wt}", f"{old_wt}")
        else:
            if not self._tauid:
                for p in self.processes:
                    self._current_df[p] = self._current_df[p].Define(f"{new_wt}", f"{old_wt} / tauSF")
            else:
                for p in self.processes:
                    self._current_df[p] = self._current_df[p].Define(
                        f"{new_wt}", f"{old_wt}")
    
    def applyTauSFAndTTBarNormAndWeightStep1(self, old_wt, new_wt, rwt1d=None, norm_factor=0.931):
        """
        rwt1d is (varName, header_path)
        apply on the original df, apply the weights based on njets
        [x] declare if the name of objects are not in the dynamic scopes
        """
        if rwt1d:
            for i in range(2, 11):
                suffix = f"_{i}jets"
                rtf = R.TFile(
                    f"{os.getcwd()}/rootfiles/func{suffix}.root")
                R.gInterpreter.ProcessLine(f"TH1* hCorr{suffix} = (TH1*)Rw1DHist{suffix}->Clone(); hCorr{suffix}->SetDirectory(0);")
            R.gInterpreter.Declare(f"#include \"{rwt1d[1]}\"")
            ttbarWeight = f"(float)eval_reweighter_njets(n_jets, {rwt1d[0]})"
            if not self._tauid:
                for p in self.processes:
                    # NOTE: hardcoded name but should be safe, since process names are unique
                    if p.startswith("ttbar"):
                        self.df[p] = self.df[p].Define(
                            f"{new_wt}", f"{old_wt} / tauSF * {ttbarWeight} * {norm_factor}")
                    else:
                        self.df[p] = self.df[p].Define(f"{new_wt}", f"{old_wt} / tauSF")
            else:
                for p in self.processes:
                    # NOTE: hardcoded name but should be safe, since process names are unique
                    if p.startswith("ttbar"):
                        self.df[p] = self.df[p].Define(
                            f"{new_wt}", f"{old_wt} * {ttbarWeight} * {norm_factor}")
                    else:
                        self.df[p] = self.df[p].Define(
                            f"{new_wt}", f"{old_wt}")
        else:
            if not self._tauid:
                for p in self.processes:
                    self.df[p] = self.df[p].Define(f"{new_wt}", f"{old_wt} / tauSF")
            else:
                for p in self.processes:
                    self.df[p] = self.df[p].Define(
                        f"{new_wt}", f"{old_wt}")

    def applyWeightStep2(self, old_wt, new_wt, rwt1d=None, declare=False):
        """
        rwt1d is (varName, header_path)
        apply on the original df, apply the weights based on dRbb
        declare if the name of objects are not in the dynamic scopes

        @note: this will not be used for resonance analysis
        """
        if rwt1d:
            suffix = "_dRbb"
            rtf = R.TFile(
                f"{os.getcwd()}/rootfiles/func{suffix}.root")
            R.gInterpreter.ProcessLine(f"TH1* hCorr{suffix} = (TH1*)Rw1DHist{suffix}->Clone(); hCorr{suffix}->SetDirectory(0);")
            R.gInterpreter.Declare(f"#include \"{rwt1d[1]}\"")
            ttbarWeight = f"(float)eval_reweighter{suffix}({rwt1d[0]})"
            for p in self.processes:
                # NOTE: hardcoded name but should be safe, since process names are unique
                if p.startswith("ttbar"):
                    self.df[p] = self.df[p].Define(
                        f"{new_wt}", f"{old_wt} * {ttbarWeight}")
                else:
                    self.df[p] = self.df[p].Define(f"{new_wt}", f"{old_wt}")
        else:
            for p in self.processes:
                self.df[p] = self.df[p].Define(f"{new_wt}", f"{old_wt}")

    def applyWeightStep3(self, old_wt, new_wt, rwt1d=None, declare=False):
        """
        rwt1d is (varName, header_path)
        apply on the original df, apply the weights based on dRbb
        declare if the name of objects are not in the dynamic scopes
        
        @note: this will not be used for resonance analysis
        """
        if rwt1d:
            suffix = "_dRlh"
            rtf = R.TFile(
                f"{os.getcwd()}/rootfiles/func{suffix}.root")
            R.gInterpreter.ProcessLine(f"TH1* hCorr{suffix} = (TH1*)Rw1DHist{suffix}->Clone(); hCorr{suffix}->SetDirectory(0);")
            R.gInterpreter.Declare(f"#include \"{rwt1d[1]}\"")
            ttbarWeight = f"(float)eval_reweighter{suffix}({rwt1d[0]})"
            for p in self.processes:
                # NOTE: hardcoded name but should be safe, since process names are unique
                if p.startswith("ttbar"):
                    self.df[p] = self.df[p].Define(
                        f"{new_wt}", f"{old_wt} * {ttbarWeight}")
                else:
                    self.df[p] = self.df[p].Define(f"{new_wt}", f"{old_wt}")
        else:
            for p in self.processes:
                self.df[p] = self.df[p].Define(f"{new_wt}", f"{old_wt}")


class AnaTTbarIncl(AnaBase):
    def __init__(self, tauid, isOS=None, prong=None, morecut=None, rewrite=None, path=None):
        super().__init__(tauid, isOS, prong, morecut, rewrite, path)

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
    def __init__(self, tauid, isOS=None, prong=None, morecut=None, rewrite=None, path=None):
        super().__init__(tauid, isOS, prong, morecut, rewrite, path)

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

        self.df["ttbarTrue"] = self.df["ttbarIncl"].Filter("!is_fake")
        self.samples.update({"ttbarTrue" : {"ttbarTrue"}})
        self.df["ttbarFake"] = self.df["ttbarIncl"].Filter("is_fake")
        self.samples.update({"ttbarFake" : {"ttbarFake"}})

        # remove the inclusive ttbar dataframe
        self.samples.pop("ttbar")
        self.df.pop("ttbarIncl")

        # refresh the processes list
        self.processes.clear()
        for label, pros in self.samples.items():
            for p in pros:
                self.processes.add(p)

        for p in self.processes:
            self.df[p] = self.df[p].Filter(reg[self._region])
        
        self._current_df = self.df
