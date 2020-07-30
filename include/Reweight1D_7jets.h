float eval_reweighter_7jets(float x) {
    return myfunc_7jets->GetBinContent(myfunc_7jets->FindBin(x));
}
