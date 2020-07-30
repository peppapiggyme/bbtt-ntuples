float eval_reweighter_10jets(float x) {
    return myfunc_10jets->GetBinContent(myfunc_10jets->FindBin(x));
}
