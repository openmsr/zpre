#!/bin/bash

set -ex

count=$(ls -1q h5m_files/rod_worth* | wc -l)
if (($count == 32)); then
  python ./scripts/ARE_rod_worth.py
  python ./scripts/ARE_rod_worth_post.py
elif (($count == 0)); then
  python ./step_to_h5m/step_to_h5m_rod_worth.py
  python ./scripts/ARE_rod_worth.py
  python ./scripts/ARE_rod_worth_post.py
else
  echo "rod worth directory incomplete"
fi
