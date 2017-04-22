#!/bin/zsh
# Generates the application UI Python file from the Qt UI file
if [ "$#" -ne 1 ] || [ ! -f "$1" ]; then
	echo >&2 "Usage: $0 <uifile>"
	exit 1
fi
uifile=$1
pyfile=$(echo $1 | sed -E 's/\.ui/.py/')
command -v pyuic4 >/dev/null 2>&1 || { echo >&2 "Unable to find pyuic4.  Aborting."; exit 1; }
pyuic4 $uifile | sed -E 's/^(class[^(]+)\(object\)\:$/\1\(QtGui.QDockWidget\):/' > $pyfile
