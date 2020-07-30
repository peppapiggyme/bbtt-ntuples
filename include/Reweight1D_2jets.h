float eval_reweighter_2jets(float x) {
    return myfunc_2jets->GetBinContent(myfunc_2jets->FindBin(x));
}
