#!/bin/zsh
currenttime=$(date '+%Y-%m-%d_%H-%M-%S')
builddir=$(pwd)'/../../build_'$currenttime
mkdir $builddir
cp *.py $builddir
cp metadata.txt $builddir
cp *.svg $builddir
if [ "$#" -eq 1 ] && [ "$1" = "-i" ]; then
    rm -fr ~/.qgis2/python/plugins/hmv/*
    cp -R "$builddir/"* ~/.qgis2/python/plugins/hmv/
fi
