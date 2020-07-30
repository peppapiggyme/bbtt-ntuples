float eval_reweighter_6jets(float x) {
    return myfunc_6jets->GetBinContent(myfunc_6jets->FindBin(x));
}
