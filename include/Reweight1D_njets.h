#ifndef REWEIGHT1D_NJETS_H
#define REWEIGHT1D_NJETS_H

float eval_reweighter_njets(int n, float x) {
    if (n == 2) {
        return hCorr_2jets->GetBinContent(hCorr_2jets->FindBin(x));
    }

    if (n == 3) {
        return hCorr_3jets->GetBinContent(hCorr_3jets->FindBin(x));
    }

    if (n == 4) {
        return hCorr_4jets->GetBinContent(hCorr_4jets->FindBin(x));
    }

    if (n == 5) {
        return hCorr_5jets->GetBinContent(hCorr_5jets->FindBin(x));
    }

    if (n == 6) {
        return hCorr_6jets->GetBinContent(hCorr_6jets->FindBin(x));
    }

    if (n == 7) {
        return hCorr_7jets->GetBinContent(hCorr_7jets->FindBin(x));
    }

    if (n == 8) {
        return hCorr_8jets->GetBinContent(hCorr_8jets->FindBin(x));
    }

    if (n == 9) {
        return hCorr_9jets->GetBinContent(hCorr_9jets->FindBin(x));
    }

    if (n >= 10) {
        return hCorr_10jets->GetBinContent(hCorr_10jets->FindBin(x));
    }

    return 1.0;
}

#endif
