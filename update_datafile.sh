#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Usage: update_datafile.sh <SDK Key>"
    exit 0
fi

DATAFILE_URL="https://cdn.optimizely.com/datafiles/$1.json"
DESTINATION_FILE="datafile.json"

curl $DATAFILE_URL > $DESTINATION_FILE