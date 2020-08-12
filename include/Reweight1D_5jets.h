#ifndef REWEIGHT1D_5JETS
#define REWEIGHT1D_5JETS
float eval_reweighter_5jets(float x) {
    return hCorr_5jets->GetBinContent(hCorr_5jets->FindBin(x));
}
#endif /* REWEIGHT1D_5JETS */
