float eval_reweighter_4jets(float x) {
    return myfunc_4jets->GetBinContent(myfunc_4jets->FindBin(x));
}
