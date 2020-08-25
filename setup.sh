# on lxplus
lsetup "lcgenv -p LCG_97python3 x86_64-centos7-gcc9-opt ROOT"

# make directories
mkdir -p rootfiles
mkdir -p plots && cd $_
mkdir -p 10jets 2jets  3jets  4jets  5jets  6jets  7jets  8jets  9jets  dRbb   dRlh   njets   test   after tau_pt fakerate
cd -
