# zpre
detailed cad model and simulations of the [zpre](https://www.osti.gov/servlets/purl/4673343) (zero power reflector-moderated reactor experiment at elevated temperature, sometimes refered to in documentation as the pr-mark I (pratt and whitney mark I).), operated by oak ridge national laboratory 1957

## model

cad model of the are can be found [here](https://cad.onshape.com/documents/c51fcabf7b4a45b5a8d610d5/v/1e941e226a75c4f4f3cbe020/e/4c356de19c02efb455bb582a) on onshape. note, the step files for the simulations (found in the step_files folder) come from the [final_for_export](https://cad.onshape.com/documents/c51fcabf7b4a45b5a8d610d5/w/a34269ffec50905ef4b5f5db/e/4c356de19c02efb455bb582a?renderMode=0&uiState=62b09138d87c8f59e3122317) branch. currently onshape does not properly export enclosed volumes, so some parts need to be modified in order to be meshed properly. additionally, one of the splines of the inner core shell was replaced with a linear approximation due to meshing issues. 

a writeup of the design, material characteristics and associated assumptions can be found in `docs/zpre.pdf`

### zpre core 
![](figures/core.png)

## prerequisites 
### cad_to_h5m
python package used to automate cubit-dagmc workflow for creating h5m files. these scripts use the [move_volumes](https://github.com/openmsr/cad_to_h5m/tree/move_volumes) branch 

### cubit
cubit is required to convert the cad model (.step) into a .h5m file readable by openmc, using the [cad_to_h5m](https://github.com/openmsr/cad_to_h5m/tree/material_tag) package. the step_to_h5m folder contains the necessary scripts for these examples. if your cubit installation is somewhere other than `/opt/Coreform-Cubit-2021.5/bin/`, you will need to update the `local_cubit_path` variable in the step_to_h5m scripts

### openmc
these simulations use [openmc](https://docs.openmc.org/en/stable/). automated source installation scripts for linux can be found [here](https://github.com/openmsr/openmc_install_scripts)

## simulation guide

first, clone the repository

```
git clone https://github.com/openmsr/zpre.git
```

enter the zpre folder and run the `run.sh` script

```
cd zpre
bash run.sh
```
