#ifndef REWEIGHT1D_10JETS
#define REWEIGHT1D_10JETS
float eval_reweighter_10jets(float x) {
    return hCorr_10jets->GetBinContent(hCorr_10jets->FindBin(x));
}
#endif /* REWEIGHT1D_10JETS */
