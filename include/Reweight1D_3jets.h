float eval_reweighter_3jets(float x) {
    return myfunc_3jets->GetBinContent(myfunc_3jets->FindBin(x));
}
