#ifndef REWEIGHT1D_DRLH
#define REWEIGHT1D_DRLH
float eval_reweighter_dRlh(float x) {
    return hCorr_dRlh->GetBinContent(hCorr_dRlh->FindBin(x));
}
#endif /* REWEIGHT1D_DRLH */
