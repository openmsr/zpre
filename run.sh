#!/bin/bash

set -ex

PS3='ZPRE simulations: '
options=("k eigenvalue" "geometry plot" "neutron flux" "photon flux" 
         "neutron flux distribution" "rod worth" "fuel height" 
         "neutron leakage" "quit")
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
        "neutron flux")
            echo "generating neutron flux plot..." &&
            bash ./scripts/nf.sh
            ;;
        "photon flux")
            echo "generating photon flux plot..." &&
            bash ./scripts/pf.sh
            ;;
        "neutron flux distribution")
            echo "generating neutron flux distributions..." &&
            bash ./scripts/nfd.sh
            ;;
        "rod worth")
            echo "generating rod worth plots..." &&
            bash ./scripts/rw.sh
            ;;
        "fuel height")
            echo "generating fuel height vs k plot..." &&
            bash ./scripts/fh.sh
            ;;
        "neutron leakage")
            echo "generating relative counting rate plot..." &&
            bash ./scripts/nl.sh
            ;;
        "quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
