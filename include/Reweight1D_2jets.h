float eval_reweighter_2jets(float x) {
    return hCorr_2jets->GetBinContent(hCorr_2jets->FindBin(x));
}
