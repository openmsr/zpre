#!/bin/bash

set -ex

if test -f "./h5m_files/zpre.h5m"; then
  python ./scripts/zpre_geometry_plot.py
else
  python ./scripts/step_to_h5m_zpre.py
  python ./scripts/zpre_geometry_plot.py
fi
