float eval_reweighter_dRlh(float x) {
    return myfunc_dRlh->GetBinContent(myfunc_dRlh->FindBin(x));
}
