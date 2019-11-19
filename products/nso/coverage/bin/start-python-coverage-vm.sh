#!/bin/sh

pypath="${NCS_DIR}/src/ncs/pyapi"

# Make sure everyone finds the NCS Python libraries at startup
if [ "x$PYTHONPATH" != "x" ]; then
    PYTHONPATH=${pypath}:$PYTHONPATH
else
    PYTHONPATH=${pypath}
fi
export PYTHONPATH

main="${pypath}/ncs_pyvm/startup.py"

echo "Starting ${main} $*"
export PYTHONUNBUFFERED=x
exec coverage run --parallel-mode ${main} $*

