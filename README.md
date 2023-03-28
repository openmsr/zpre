# zpre
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

detailed cad model and simulations of the [zpre](https://www.osti.gov/servlets/purl/4673343) (zero power reflector-moderated reactor experiment at elevated temperature, sometimes refered to in documentation as the pr-mark I (pratt and whitney mark I).), operated by oak ridge national laboratory 1957

## model

### zpre core 
![](figures/core.png)

Work-in-progress cad model of the zpre can be found [here](https://cad.onshape.com/documents/c51fcabf7b4a45b5a8d610d5/w/a34269ffec50905ef4b5f5db/e/4c356de19c02efb455bb582a?renderMode=0&uiState=62d54b7b4c1a0504f9194fa8) on onshape.

Note that this work and the cad model is under the GNU General Public License v3.0

## prerequisites
### CAD_to_openMC
[CAD_to_openMC](https://github.com/openmsr/CAD_to_openMC) is an open-source package to convert CAD geometry (in the form of '.step' files) into an openmc-readable h5m file

### openmc
These simulations use [openmc](https://docs.openmc.org/en/stable/). Automated source installation scripts for linux can be found [here](https://github.com/openmsr/openmc_install_scripts)

## simulation guide

First, clone the repository

```
git clone https://github.com/openmsr/zpre.git
```

Second, enter the zpre folder and run the `run.sh` script

```
cd zpre
bash run.sh
```
