float eval_reweighter_6jets(float x) {
    return hCorr_6jets->GetBinContent(hCorr_6jets->FindBin(x));
}
