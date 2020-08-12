#ifndef REWEIGHT1D_3JETS
#define REWEIGHT1D_3JETS
float eval_reweighter_3jets(float x) {
    return hCorr_3jets->GetBinContent(hCorr_3jets->FindBin(x));
}
#endif /* REWEIGHT1D_3JETS */
