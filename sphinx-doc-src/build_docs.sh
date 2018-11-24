#!/bin/bash
script_location="$(dirname $0)"
sphinx-build -b html ${script_location)/source ${script_location}/../../HMV-meretezes-docs/docs/ 
