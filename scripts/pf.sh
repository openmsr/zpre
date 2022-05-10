#!/bin/bash

set -ex

if test -f "./h5m_files/zpre.h5m"; then
  python ./scripts/zpre_photon_flux.py
else
  python ./step_to_h5m/step_to_h5m_zpre.py
  python ./scripts/zpre_photon_flux.py
fi
