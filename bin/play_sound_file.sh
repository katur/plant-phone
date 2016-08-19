#!/bin/sh

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
fi

aplay $1
