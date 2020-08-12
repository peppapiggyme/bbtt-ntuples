#ifndef REWEIGHT1D_7JETS
#define REWEIGHT1D_7JETS
float eval_reweighter_7jets(float x) {
    return hCorr_7jets->GetBinContent(hCorr_7jets->FindBin(x));
}
#endif /* REWEIGHT1D_7JETS */
