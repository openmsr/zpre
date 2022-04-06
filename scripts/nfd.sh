#!/bin/bash

set -ex

if test -f "./h5m_files/zpre.h5m"; then
  python ./scripts/zpre_neutron_flux_foils.py
  python ./scripts/zpre_neutron_flux_foils_post.py
else
  python ./step_to_h5m/step_to_h5m_zpre.py
  python ./scripts/zpre_neutron_flux_foils.py
  python ./scripts/zpre_neutron_flux_foils_post.py
fi
