float eval_reweighter_9jets(float x) {
    return myfunc_9jets->GetBinContent(myfunc_9jets->FindBin(x));
}
