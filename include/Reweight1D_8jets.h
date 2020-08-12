#ifndef REWEIGHT1D_8JETS
#define REWEIGHT1D_8JETS
float eval_reweighter_8jets(float x) {
    return hCorr_8jets->GetBinContent(hCorr_8jets->FindBin(x));
}
#endif /* REWEIGHT1D_8JETS */
