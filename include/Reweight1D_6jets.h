#ifndef REWEIGHT1D_6JETS
#define REWEIGHT1D_6JETS
float eval_reweighter_6jets(float x) {
    return hCorr_6jets->GetBinContent(hCorr_6jets->FindBin(x));
}
#endif /* REWEIGHT1D_6JETS */
