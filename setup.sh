# on lxplus
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh --quiet
lsetup "lcgenv -p LCG_97python3 x86_64-centos7-gcc9-opt ROOT" --quiet

# make directories
mkdir -p rootfiles
mkdir -p plots && cd $_
mkdir -p 10jets 2jets  3jets  4jets  5jets  6jets  7jets  8jets  9jets  dRbb   dRlh   njets   test   after tau_pt fakerate
cd -
