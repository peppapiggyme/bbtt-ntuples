# put tmp code here

# rwt_lep_pt = TTbarTrueFakePlot(rwt, "lep_pt", "weight", (380, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_lep_pt, "lepton pT [MeV]", regionTeX, f"plots/{i}jets/stack_lep_pt_fr_os" + suffix_before)

# rwt_met = TTbarTrueFakePlot(rwt, "MET", "weight", (400, 0, 400000), array.array(
#     'd', [i for i in range(0, 420000, 20000)]))
# drawStack(rwt_met, "MET [MeV]", regionTeX, f"plots/{i}jets/stack_met_fr_os" + suffix_before)

# rwt_metsig = TTbarTrueFakePlot(rwt, "METSig", "weight", (20, 0, 20))
# drawStack(rwt_metsig, "MET Significance", regionTeX, f"plots/{i}jets/stack_metsig_fr_os" + suffix_before)

# rwt_tau_pt = TTbarTrueFakePlot(rwt, "tau_pt", "weight", (980, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_tau_pt, "tau pT [MeV]", regionTeX, f"plots/{i}jets/stack_tau_pt_fr_os" + suffix_before)

# rwt_b0_pt = TTbarTrueFakePlot(rwt, "b0_pt", "weight", (980, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_b0_pt, "leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b0_pt_fr_os" + suffix_before)

# rwt_b1_pt = TTbarTrueFakePlot(rwt, "b1_pt", "weight", (980, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_b1_pt, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b1_pt_fr_os" + suffix_before)

# rwt_mtw = TTbarTrueFakePlot(rwt, "mTW", "weight", (200, 40000, 240000), array.array(
#     'd', [i for i in range(50000, 260000, 10000)]))
# drawStack(rwt_mtw, "M_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_mtw_fr_os" + suffix_before)

# rwt_mbb = TTbarTrueFakePlot(rwt, "mBB", "weight", (500, 150000, 650000), array.array(
#     'd', [i for i in range(150000, 670000, 20000)]))
# drawStack(rwt_mbb, "Mbb [MeV]", regionTeX, f"plots/{i}jets/stack_mbb_fr_os" + suffix_before)

# rwt_mhh = TTbarTrueFakePlot(rwt, "mHH", "weight", (2000, 200000, 2200000), array.array(
#     'd', [i for i in range(200000, 2200000, 50000)]))
# drawStack(rwt_mhh, "Mhh [MeV]", regionTeX, f"plots/{i}jets/stack_mhh_fr_os" + suffix_before)

# rwt_lep_pt = TTbarTrueFakePlot(rwt, "lep_pt", "weight_new", (380, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_lep_pt, "lepton pT [MeV]", regionTeX, f"plots/{i}jets/stack_lep_pt_fr_os" + suffix_after)

# rwt_met = TTbarTrueFakePlot(rwt, "MET", "weight_new", (400, 0, 400000), array.array(
#     'd', [i for i in range(0, 420000, 20000)]))
# drawStack(rwt_met, "MET [MeV]", regionTeX, f"plots/{i}jets/stack_met_fr_os" + suffix_after)

# rwt_metsig = TTbarTrueFakePlot(rwt, "METSig", "weight_new", (20, 0, 20))
# drawStack(rwt_metsig, "MET Significance", regionTeX, f"plots/{i}jets/stack_metsig_fr_os" + suffix_after)

# rwt_tau_pt = TTbarTrueFakePlot(rwt, "tau_pt", "weight_new", (980, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_tau_pt, "tau pT [MeV]", regionTeX, f"plots/{i}jets/stack_tau_pt_fr_os" + suffix_after)

# rwt_b0_pt = TTbarTrueFakePlot(rwt, "b0_pt", "weight_new", (980, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_b0_pt, "leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b0_pt_fr_os" + suffix_after)

# rwt_b1_pt = TTbarTrueFakePlot(rwt, "b1_pt", "weight_new", (980, 20000, 1000000), array.array(
#     'd', [20000, 30000, 40000, 50000, 60000, 70000, 90000, 120000, 160000, 250000, 1000000]))
# drawStack(rwt_b1_pt, "sub-leading b-jet pT [MeV]", regionTeX, f"plots/{i}jets/stack_b1_pt_fr_os" + suffix_after)

# rwt_mtw = TTbarTrueFakePlot(rwt, "mTW", "weight_new", (200, 40000, 240000), array.array(
#     'd', [i for i in range(50000, 260000, 10000)]))
# drawStack(rwt_mtw, "M_{T} [MeV]", regionTeX, f"plots/{i}jets/stack_mtw_fr_os" + suffix_after)

# rwt_mbb = TTbarTrueFakePlot(rwt, "mBB", "weight_new", (500, 150000, 650000), array.array(
#     'd', [i for i in range(150000, 670000, 20000)]))
# drawStack(rwt_mbb, "Mbb [MeV]", regionTeX, f"plots/{i}jets/stack_mbb_fr_os" + suffix_after)

# rwt_mhh = TTbarTrueFakePlot(rwt, "mHH", "weight_new", (2000, 200000, 2200000), array.array(
#     'd', [i for i in range(200000, 2200000, 50000)]))
# drawStack(rwt_mhh, "Mhh [MeV]", regionTeX, f"plots/{i}jets/stack_mhh_fr_os" + suffix_after)
