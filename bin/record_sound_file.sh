#!/bin/sh

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
fi

arecord -D plughw:1,0 $1
