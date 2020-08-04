float eval_reweighter_4jets(float x) {
    return hCorr_4jets->GetBinContent(hCorr_4jets->FindBin(x));
}
