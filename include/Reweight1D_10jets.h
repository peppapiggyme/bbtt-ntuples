float eval_reweighter_10jets(float x) {
    return hCorr_10jets->GetBinContent(hCorr_10jets->FindBin(x));
}
