#!/bin/bash
# SCRIPT SUMMARY
# 1. Creates an INI file if it doesn't exist
# 2. Stores log and working directory in INI config
# 3. Copies the necessary plugin files to the build directory
# 4. Creates the QGIS plugin directory if it doesn't exist
# 5. Copies the plugin files from the build to the plugin directory
currenttime=$(date '+%Y-%m-%d_%H-%M-%S')
projdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"

if [ ! -f "$projdir/hmv_meretezes_plugin.py" ];then
    echo "ERROR: this script needs to be located in the project directory!"
    exit 1
fi

builddir="$projdir"'/../build/build_'$currenttime
plugindir=~/.qgis2/python/plugins/hmv/

if [ ! -f "${projdir}/hmv.ini" ]; then
	echo "No ini file, creating..."
	echo '[hmv]' > "${projdir}"/hmv.ini
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

	echo "logdir=$logpath" >> "${projdir}"/hmv.ini
	echo "workdir=$workdir" >> "${projdir}"/hmv.ini
fi

mkdir -p $builddir
cp -v "${projdir}"/*.py $builddir
cp -v "${projdir}"/metadata.txt $builddir
cp -v "${projdir}"/*.svg $builddir
cp -v "${projdir}"/*.ini $builddir

if [ "$#" -eq 1 ] && [ "$1" = "-i" ]; then
	[ ! -d "$plugindir" ] && mkdir -p "$plugindir"
	rm -frv "${plugindir}/"*
	cp -v -R "${builddir}/"* "$plugindir"
fi
