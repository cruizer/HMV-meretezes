#!/bin/zsh
# Generates the application UI Python file from the Qt UI file
if [ "$#" -ne 1 ] || [ ! -f "$1" ]; then
	echo >&2 "Usage: $0 <uifile>"
	exit 1
fi
uifile=$1
pyfile=$(echo $1 | sed -E 's/\.ui/.py/')
python /usr/lib/python2.7/dist-packages/qgis/PyQt/uic/pyuic.py $uifile | sed -E 's/^(class[^(]+)\(object\)\:$/\1\(QtGui.QDockWidget\):/' > $pyfile
