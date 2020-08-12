#ifndef REWEIGHT1D_9JETS
#define REWEIGHT1D_9JETS
float eval_reweighter_9jets(float x) {
    return hCorr_9jets->GetBinContent(hCorr_9jets->FindBin(x));
}
#endif /* REWEIGHT1D_9JETS */
