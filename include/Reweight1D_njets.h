float eval_reweighter_njets(int n, float x) {
    if (n == 2) {
        return myfunc_2jets->GetBinContent(myfunc_2jets->FindBin(x));
    }

    if (n == 3) {
        return myfunc_3jets->GetBinContent(myfunc_3jets->FindBin(x));
    }

    if (n == 4) {
        return myfunc_4jets->GetBinContent(myfunc_4jets->FindBin(x));
    }

    if (n == 5) {
        return myfunc_5jets->GetBinContent(myfunc_5jets->FindBin(x));
    }

    if (n == 6) {
        return myfunc_6jets->GetBinContent(myfunc_6jets->FindBin(x));
    }

    if (n == 7) {
        return myfunc_7jets->GetBinContent(myfunc_7jets->FindBin(x));
    }

    if (n == 8) {
        return myfunc_8jets->GetBinContent(myfunc_8jets->FindBin(x));
    }

    if (n == 9) {
        return myfunc_9jets->GetBinContent(myfunc_9jets->FindBin(x));
    }

    if (n >= 10) {
        return myfunc_10jets->GetBinContent(myfunc_10jets->FindBin(x));
    }

    return 1.0;
}
