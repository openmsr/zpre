#!/bin/bash

set -ex

count=$(ls -1q h5m_files/fuel_height* | wc -l)
if (($count == 5)); then
  python ./scripts/zpre_fuel_height.py
else
  python ./step_to_h5m/step_to_h5m_fuel_height.py
  python ./scripts/zpre_fuel_height.py
fi
