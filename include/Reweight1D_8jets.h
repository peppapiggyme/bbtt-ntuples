float eval_reweighter_8jets(float x) {
    return myfunc_8jets->GetBinContent(myfunc_8jets->FindBin(x));
}
