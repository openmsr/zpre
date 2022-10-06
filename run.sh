#!/bin/bash

set -ex

PS3='ZPRE simulations: '
options=("k eigenvalue" "geometry plot" "geometry voxelplot" "neutron flux" "neutron flux 3d" "photon flux" "quit")
select opt in "${options[@]}"
do
    case $opt in
        "k eigenvalue")
            echo "running k eigenvalue simulation..." &&
            bash ./scripts/k.sh
            ;;
        "geometry plot")
            echo "plotting geometry..." &&
            bash ./scripts/gp.sh
            ;;
        "geometry voxelplot")
            echo "plotting geometry in 3d..." &&
            bash ./scripts/vp.sh
            ;;
        "neutron flux")
            echo "generating neutron flux plot..." &&
            bash ./scripts/nf.sh
            ;;
        "neutron flux 3d")
            echo "generating neutron flux 3d voxel data..." &&
            bash ./scripts/nf3d.sh
            ;;
        "photon flux")
            echo "generating photon flux plot..." &&
            bash ./scripts/pf.sh
            ;;
        "quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
