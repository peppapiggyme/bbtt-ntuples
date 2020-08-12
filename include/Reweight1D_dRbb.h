#ifndef REWEIGHT1D_DRBB
#define REWEIGHT1D_DRBB
float eval_reweighter_dRbb(float x) {
    return hCorr_dRbb->GetBinContent(hCorr_dRbb->FindBin(x));
}
#endif /* REWEIGHT1D_DRBB */
