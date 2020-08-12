#ifndef REWEIGHT1D_4JETS
#define REWEIGHT1D_4JETS
float eval_reweighter_4jets(float x) {
    return hCorr_4jets->GetBinContent(hCorr_4jets->FindBin(x));
}
#endif /* REWEIGHT1D_4JETS */
