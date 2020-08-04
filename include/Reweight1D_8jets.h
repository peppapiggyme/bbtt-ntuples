float eval_reweighter_8jets(float x) {
    return hCorr_8jets->GetBinContent(hCorr_8jets->FindBin(x));
}
