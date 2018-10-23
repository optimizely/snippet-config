#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Usage: update_datafile.sh <SDK Key>"
    echo "Example: update_datafile.sh FTTcU3Li4Ru1DA3LnvSMns"
    exit 0
fi

DATAFILE_URL="https://cdn.optimizely.com/datafiles/$1.json"
DESTINATION_FILE="datafile.json"

echo "Fetching datafile from $DATAFILE_URL"
curl $DATAFILE_URL > $DESTINATION_FILE
curl http://localhost:4001/refresh