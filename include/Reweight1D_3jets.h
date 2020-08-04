float eval_reweighter_3jets(float x) {
    return hCorr_3jets->GetBinContent(hCorr_3jets->FindBin(x));
}
