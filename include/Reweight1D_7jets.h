float eval_reweighter_7jets(float x) {
    return hCorr_7jets->GetBinContent(hCorr_7jets->FindBin(x));
}
