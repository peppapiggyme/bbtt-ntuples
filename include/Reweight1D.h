float eval_reweighter1d(float x) {
    return myfunc->Eval(TMath::Min(x, 1000000.0f));
}
