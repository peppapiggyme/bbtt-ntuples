Dependence: ROOT6.22 + python3

installation
```shell
# conda env create -f CondaEnv.yml
conda create -c conda-forge --name cern root
conda activate cern
conda install uproot matplotlib
```

ttbar reweighting factor calculation: three steps in one script
```
python t_reweighter.py
```

check the correlation of the variables that are used for parrametrisation
```
python t_checkCorrelation.py
```

apply reweight
```
python t_applyReweight_id.py
python t_applyReweight_noid.py
```

derive non-closure uncertainties
```
python t_reweightClosure.py
```

check the reweighting systematics: need to run on post-reweighting ntuples
```
python t_reweightSyst_id.py
python t_reweightSyst_noid.py
```

calculate fake rates: so far run on pre-reweighting ntuples
```
python t_fakerate.py
```
