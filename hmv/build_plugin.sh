#!/bin/bash
currenttime=$(date '+%Y-%m-%d_%H-%M-%S')
builddir=$(pwd)'/../build/build_'$currenttime
plugindir=~/.qgis2/python/plugins/hmv/
if [ ! -f hmv.ini ]; then
	echo "No ini file, creating..."
	echo '[hmv]' > hmv.ini
	while [ ! -d "$logpath" ];do
		[ ! -z ${logpath+x} ] && echo "Directory $logpath doesn't exist!"
		echo -n 'Plugin logs should be put in directory (absolute path): '
		read logpath
	done
	while [ ! -d "$workdir" ];do
		[ ! -z ${workdir+x} ] && echo "Directory $workdir doesn't exist!"
		echo -n 'Layer working directory where data will be saved (absolute path): '
		read workdir
	done

	echo "logdir=$logpath" >> hmv.ini
	echo "workdir=$workdir" >> hmv.ini
fi
mkdir $builddir
cp *.py $builddir
cp metadata.txt $builddir
cp *.svg $builddir
cp *.ini $builddir
if [ "$#" -eq 1 ] && [ "$1" = "-i" ]; then
	[ ! -d "$plugindir" ] && mkdir $plugindir
	rm -fr ~/.qgis2/python/plugins/hmv/*
	cp -R "$builddir/"* ~/.qgis2/python/plugins/hmv/
fi
