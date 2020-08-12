#ifndef REWEIGHT1D_2JETS
#define REWEIGHT1D_2JETS
float eval_reweighter_2jets(float x) {
    return hCorr_2jets->GetBinContent(hCorr_2jets->FindBin(x));
}
#endif /* REWEIGHT1D_2JETS */
