#!/bin/bash

set -ex

if test -f "./h5m_files/zpre.h5m"; then
  python ./scripts/zpre_neutron_flux3d.py
else
  python ./scripts/step_to_h5m_zpre.py
  python ./scripts/zpre_neutron_flux3d.py
fi
