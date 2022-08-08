#!/bin/sh
cd os 
timeout 1800 make run > ../output
status=$?
if [ $status -eq 124 ] #timed out
then
    exit 0
fi
exit $status
cd ..
python3 test.py < output